from __future__ import absolute_import, division, print_function, unicode_literals

from functools import wraps

import django_agent_trust.conf
import django_otp.conf
from django_otp.decorators import otp_required as real_otp_required


def otp_required(view=None, redirect_field_name='next', login_url=None, if_configured=False, accept_trusted_agent=False):
    """
    Similar to :func:`~django_otp.decorators.otp_required`, but with an extra
    argument.

    The default value for ``login_url`` depends on the value of
    ``accept_trusted_agent``. If ``True``, we'll use
    :setting:`AGENT_LOGIN_URL`; otherwise, we'll use :setting:`OTP_LOGIN_URL`.

    :param bool accept_trusted_agent: If ``True``, we'll accept a trusted
        agent in lieu of OTP verification. Default is ``False``.
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if accept_trusted_agent and request.agent.is_trusted:
                _decorator = lambda v: v
            else:
                _login_url = login_url
                if _login_url is None:
                    _login_url = django_agent_trust.conf.settings.AGENT_LOGIN_URL if accept_trusted_agent else django_otp.conf.settings.OTP_LOGIN_URL
                _decorator = real_otp_required(redirect_field_name=redirect_field_name, login_url=_login_url, if_configured=if_configured)

            return _decorator(view_func)(request, *args, **kwargs)

        return _wrapped_view

    return decorator(view) if (view is not None) else decorator
