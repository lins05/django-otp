django-otp-sns
==============

.. include:: ../../README

This package uses `boto <http://pypi.python.org/pypi/boto>`_ to communicate with
AWS.


SNS Devices
-----------

.. autoclass:: otp_sns.models.SNSDevice
    :members:


Admin
-----

The following :class:`~django.contrib.admin.ModelAdmin` subclass is registered
with the default admin site. We recommend its use with custom admin sites as
well:

.. autoclass:: otp_sns.admin.SNSDeviceAdmin


Settings
--------

.. setting:: OTP_SNS_AWS_ID

**OTP_SNS_AWS_ID**

Default: ``None``

Your AWS access ID. If ``None``, boto will look for it in the usual places.


.. setting:: OTP_SNS_AWS_KEY

**OTP_SNS_AWS_KEY**

Default: ``None``

Your AWS secret access key. If ``None``, boto will look for it the usual places.


.. setting:: OTP_SNS_DEFAULT_MESSAGE

**OTP_SNS_DEFAULT_MESSAGE**

Default: ``'Sent'``

The default value for :attr:`otp_sns.models.SNSDevice.message`.


License
-------

.. include:: ../../LICENSE
