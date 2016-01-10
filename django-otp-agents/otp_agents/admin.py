from __future__ import absolute_import, division, print_function, unicode_literals

import django_otp.admin


class TrustedAgentAdminSite(django_otp.admin.OTPAdminSite):
    """
    This is an :class:`~django_otp.admin.OTPAdminSite` subclass that is
    satisfied by a trusted agent.

    This is identical to ``django_otp.admin.OTPAdminSite`` except that it will
    skip the login dialog if the user is already logged in and is either
    verified with an OTP device or is coming from a previously trusted agent.

    Note that :class:`~django.contrib.admin.AdminSite` lacks the hooks
    necessary to properly implement a trusted agent login form here. If the
    user does not meet the criteria above, they will have to verify themselves
    with an OTP device to log in. The experience will be better if you send
    users through your own custom login flow before redirecting them to this
    admin site.

    """
    def has_permission(self, request):
        return super(django_otp.admin.OTPAdminSite, self).has_permission(request) and \
            (request.user.is_verified() or request.agent.is_trusted)
