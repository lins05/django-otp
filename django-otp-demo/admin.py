from django.contrib.auth.admin import Group, GroupAdmin, User, UserAdmin

from django_otp.admin import OTPAdminSite
from django_otp.plugins.otp_static.admin import StaticDevice, StaticDeviceAdmin
from django_otp.plugins.otp_email.admin import EmailDevice, EmailDeviceAdmin
from django_otp.plugins.otp_hotp.admin import HOTPDevice, HOTPDeviceAdmin
from django_otp.plugins.otp_totp.admin import TOTPDevice, TOTPDeviceAdmin
from otp_twilio.admin import TwilioSMSDevice, TwilioSMSDeviceAdmin
from otp_yubikey.admin import YubikeyDevice, ValidationService, YubikeyDeviceAdmin
from otp_yubikey.admin import RemoteYubikeyDevice, ValidationServiceAdmin, RemoteYubikeyDeviceAdmin


site = OTPAdminSite(OTPAdminSite.name)

site.register(Group, GroupAdmin)
site.register(User, UserAdmin)
site.register(StaticDevice, StaticDeviceAdmin)
site.register(EmailDevice, EmailDeviceAdmin)
site.register(HOTPDevice, HOTPDeviceAdmin)
site.register(TOTPDevice, TOTPDeviceAdmin)
site.register(TwilioSMSDevice, TwilioSMSDeviceAdmin)
site.register(YubikeyDevice, YubikeyDeviceAdmin)
site.register(ValidationService, ValidationServiceAdmin)
site.register(RemoteYubikeyDevice, RemoteYubikeyDeviceAdmin)
