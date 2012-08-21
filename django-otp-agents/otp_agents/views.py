from functools import partial

from django.contrib.auth import BACKEND_SESSION_KEY
from django.contrib.auth.views import login as auth_login

from .forms import OTPAuthenticationForm, OTPTokenForm


def login(request, **kwargs):
    """
    This is just like :func:`django_otp.views.login` except that it uses our
    agent-trust-enabled forms.
    """
    user = request.user

    if user.is_anonymous() or user.is_verified():
        form = OTPAuthenticationForm
    else:
        form = partial(OTPTokenForm, user)

        # A minor hack to make django.contrib.auth.login happy
        user.backend = request.session[BACKEND_SESSION_KEY]

    kwargs['authentication_form'] = form

    return auth_login(request, **kwargs)
