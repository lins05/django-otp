from functools import partial

from django.contrib.auth import BACKEND_SESSION_KEY
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import login as auth_login

from .forms import OTPAuthenticationForm, OTPTokenForm


def login(request, **kwargs):
    """
    This is much like :func:`django_otp.views.login` except that it uses our
    agent-trust-enabled forms. This view tries to be clever and is only
    provided as a convenience and an example.

    If the request is from an already-trusted agent, we'll use the standard
    single-factor authentication form. Otherwise, if the user is anonymous or
    fully OTP-verified, we'll use the full two-factor authentication form.  An
    authenticated user on an untrusted agent will get the OTP-only form. In the
    second two cases, the form will include the ``otp_trust_agent`` field,
    allowing the user to indicate that OTP verification should be skipped in
    the future.
    """
    user = request.user

    if request.agent.is_trusted:
        form = AuthenticationForm
    elif user.is_anonymous() or user.is_verified():
        form = OTPAuthenticationForm
    else:
        form = partial(OTPTokenForm, user)

        # A minor hack to make django.contrib.auth.login happy
        user.backend = request.session[BACKEND_SESSION_KEY]

    kwargs['authentication_form'] = form

    return auth_login(request, **kwargs)
