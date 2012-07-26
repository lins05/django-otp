import django.conf


class Settings(object):
    """
    This is a simple class to take the place of the global settings object. An
    instance will contain all of our settings as attributes, with default values
    if they are not specified by the configuration.
    """
    defaults = {
        'OTP_SNS_AWS_ID': None,
        'OTP_SNS_AWS_KEY': None,
        'OTP_SNS_DEFAULT_REGION': 'us-east-1',
        'OTP_SNS_DEFAULT_MESSAGE': 'Sent',
    }

    def __init__(self):
        """
        Loads our settings from django.conf.settings, applying defaults for any
        that are omitted.
        """
        for name, default in self.defaults.iteritems():
            value = getattr(django.conf.settings, name, default)
            setattr(self, name, value)


settings = Settings()