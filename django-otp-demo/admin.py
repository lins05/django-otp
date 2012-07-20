from django.contrib.auth.admin import Group, GroupAdmin, User, UserAdmin

from django_otp.admin import OTPAdminSite
from django_otp.static.admin import StaticDevice, StaticDeviceAdmin
from django_otp.email.admin import EmailDevice, EmailDeviceAdmin


site = OTPAdminSite()

site.register(Group, GroupAdmin)
site.register(User, UserAdmin)
site.register(StaticDevice, StaticDeviceAdmin)
site.register(EmailDevice, EmailDeviceAdmin)
