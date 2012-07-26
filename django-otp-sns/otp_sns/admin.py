from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered

from .models import SNSDevice


class SNSDeviceAdmin(admin.ModelAdmin):
    """
    :class:`~django.contrib.admin.ModelAdmin` for
    :class:`~otp_sns.models.SNSDevice`.
    """
    fieldsets = [
        ('Identity', {
            'fields': ['user', 'name', 'confirmed'],
        }),
        ('Configuration', {
            'fields': ['topic', 'region', 'message', 'key'],
        }),
    ]


try:
    admin.site.register(SNSDevice, SNSDeviceAdmin)
except AlreadyRegistered:
    # Ignore the useless exception from multiple imports
    pass
