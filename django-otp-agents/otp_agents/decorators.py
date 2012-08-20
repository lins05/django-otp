from functools import wraps

from django_otp.decorators import otp_required as real_otp_required
from django_agent_trust.decorators import trusted_agent_required


def otp_required(view=None, redirect_field_name='next', login_url=None, accept_trusted_agent=False):
    """
    Similar to :func:`~django_otp.decorators.otp_required`, but with an extra
    argument.

    :param bool accept_trusted_agent: If ``True``, we'll accept a trusted
        agent in lieu of OTP verification. Default is ``False``.
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_verified() or (accept_trusted_agent and request.agent.is_trusted):
                x_required = lambda v: v
            elif accept_trusted_agent:
                x_required = trusted_agent_required(redirect_field_name=redirect_field_name, login_url=login_url)
            else:
                x_required = real_otp_required(redirect_field_name=redirect_field_name, login_url=login_url)

            return x_required(view_func)(request, *args, **kwargs)

        return _wrapped_view

    return decorator(view) if (view is not None) else decorator
