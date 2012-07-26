from binascii import unhexlify
from functools import partial
import logging

from boto import sns
from django.db import models

from django_otp.models import Device
from django_otp.oath import totp
from django_otp.util import random_hex, hex_validator

from .conf import settings


logger = logging.getLogger(__name__)


class SNSDevice(Device):
    """
    A device that delivers codes to an AWS SNS topic. The primary application
    of this is expected to be SMS delivery, although there's no such limitation
    in the code.

    Creating SNS topics and adding subscriptions is an exercise left to the
    client. This device only posts and verifies.

    This uses TOTP to generate temporary tokens. We use the default 30 second
    time step and allow a one step grace period.

    .. attribute:: topic

        The ARN of the SNS topic to post to.

    .. attribute:: message

        The message to show the user after posting a token. (Default:
        settings.OTP_SNS_DEFAULT_MESSAGE)

    .. attribute:: key

        The secret key used to generate TOTP tokens.
    """
    topic = models.CharField(max_length=256,
        help_text="The ARN of the SNS topic to post to."
    )

    message = models.CharField(max_length=64,
        default=settings.OTP_SNS_DEFAULT_MESSAGE,
        help_text="The message to present the user after sending the token."
    )

    key = models.CharField(max_length=40,
        validators=[hex_validator(20)],
        default=lambda: random_hex(20),
        help_text="A random key used to generate tokens (hex-encoded)."
    )

    class Meta(Device.Meta):
        verbose_name = "SNS Device"

    def __unicode__(self):
        return self.topic

    @property
    def bin_key(self):
        return unhexlify(self.key)

    def generate_challenge(self):
        """
        Generates a random token and publishes it to
        :attr:`~otp_sns.models.SNSDevice.topic`. The token will only be valid
        for a limited time. If there's an error, we'll log it and raise a
        StandardError.

        :returns: :attr:`~otp_sns.models.SNSDevice.message` on success.
        """
        token = totp(self.bin_key)

        # Special topic for test cases
        if self.topic == 'test':
            return token

        try:
            region = self.topic.split(':')[3]

            connection = sns.connect_to_region(region,
                aws_access_key_id=settings.OTP_SNS_AWS_ID,
                aws_secret_access_key=settings.OTP_SNS_AWS_KEY
            )

            result = connection.publish(self.topic, '{0:06}'.format(token))
            result['PublishResponse']['PublishResult']['MessageId']
        except StandardError as e:
            logger.error('Error posting SNS token: {0}'.format(e))
            raise StandardError('Failed to send the token')

        return self.message

    def verify_token(self, token):
        try:
            token = int(token)
        except ValueError:
            return False
        else:
            return any(totp(self.bin_key, drift=drift) == token for drift in [0, -1])
