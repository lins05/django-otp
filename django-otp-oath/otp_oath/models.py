from binascii import unhexlify

from django.db import models

from django_otp.models import Device
from django_otp.oath import hotp, totp
from django_otp.util import random_hex, hex_validator


class HOTPDevice(Device):
    """
    A generic HOTP device. The model fields correspond to the arguments to
    :func:`django_otp.oath.hotp`. They all have sensible defaults, including
    the key, which is randomly generated.

    .. attribute:: key

        A hex-encoded secret key of up to 40 bytes.

    .. atribute:: digits

        The number of digits to expect from the token generator.

    .. attribute:: drift

        The amount of counter drift to tolerate.

    .. attribute: counter

        The next counter value to expect.
    """
    key = models.CharField(max_length=80, validators=[hex_validator()], default=lambda: random_hex(20), help_text=u"A hex-encoded secret key of up to 40 bytes.")
    digits = models.PositiveSmallIntegerField(choices=[(6,6), (8,8)], default=6, help_text=u"The number of digits to expect in a token.")
    drift = models.PositiveSmallIntegerField(default=3, help_text=u"The amount of counter drift to tolerate.")
    counter = models.BigIntegerField(default=0, help_text=u"The next counter value to expect.")

    @property
    def bin_key(self):
        return unhexlify(self.key)

    def verify_token(self, token):
        try:
            token = int(token)
        except ValueError:
            verified = False
        else:
            key = self.bin_key

            for counter in range(self.counter, self.counter + self.drift + 1):
                if hotp(key, counter, self.digits) == token:
                    verified = True
                    self.counter = counter + 1
                    self.save()
                    break
            else:
                verified = False

        return verified


class TOTPDevice(Device):
    """
    A generic TOTP device. The model fields correspond to the arguments to
    :func:`django_otp.oath.totp`. They all have sensible defaults, including
    the key, which is randomly generated.

    .. attribute:: key

        A hex-encoded secret key of up to 40 bytes.

    .. attribute:: step

        The time step in seconds.

    .. attribute:: t0

        The UNIX time at which to begin counting steps.

    .. attribute:: digits

        The number of digits to expect in a token.

    .. attribute:: drift

        The number of time steps in the past to allow.
    """
    key = models.CharField(max_length=80, validators=[hex_validator()], default=lambda: random_hex(20), help_text=u"A hex-encoded secret key of up to 40 bytes.")
    step = models.PositiveSmallIntegerField(default=30, help_text=u"The time step in seconds.")
    t0 = models.BigIntegerField(default=0, help_text=u"The UNIX time at which to begin counting steps.")
    digits = models.PositiveSmallIntegerField(choices=[(6,6), (8,8)], default=6, help_text=u"The number of digits to expect in a token.")
    drift = models.PositiveSmallIntegerField(default=1, help_text=u"The number of time steps in the past to allow.")

    @property
    def bin_key(self):
        return unhexlify(self.key)

    def verify_token(self, token):
        try:
            token = int(token)
        except ValueError:
            verified = False
        else:
            key = self.bin_key

            for drift in reversed(range(-self.drift, 1)):
                if totp(key, self.step, self.t0, self.digits, drift) == token:
                    verified = True
                    break
            else:
                verified = False

        return verified
