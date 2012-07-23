from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered

from .models import HOTPDevice, TOTPDevice


class HOTPDeviceAdmin(admin.ModelAdmin):
    pass


class TOTPDeviceAdmin(admin.ModelAdmin):
    pass


try:
    admin.site.register(HOTPDevice, HOTPDeviceAdmin)
    admin.site.register(TOTPDevice, TOTPDeviceAdmin)
except AlreadyRegistered:
    # A useless exception from a double import
    pass
