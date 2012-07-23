from django.contrib.auth.admin import Group, GroupAdmin, User, UserAdmin

from django_otp.admin import OTPAdminSite
from django_otp.plugins.otp_static.admin import StaticDevice, StaticDeviceAdmin
from django_otp.plugins.otp_email.admin import EmailDevice, EmailDeviceAdmin
from otp_yubikey.admin import YubikeyDevice, YubikeyDeviceAdmin
from otp_yubikey.admin import RemoteYubikeyDevice, RemoteYubikeyDeviceAdmin


site = OTPAdminSite()

site.register(Group, GroupAdmin)
site.register(User, UserAdmin)
site.register(StaticDevice, StaticDeviceAdmin)
site.register(EmailDevice, EmailDeviceAdmin)
site.register(YubikeyDevice, YubikeyDeviceAdmin)
site.register(RemoteYubikeyDevice, RemoteYubikeyDeviceAdmin)
