"""
This package provides subclasses of
:class:`~django_otp.forms.OTPAuthenticationForm` and
:class:`~django_otp.forms.OTPTokenForm` with an extra boolean field called
``otp_trust_agent``. The user can check this option to indicate that they'd
like to bypass OTP verification when accessing the site from the same browser
in the future.

When these forms are used with :func:`django.contrib.auth.views.login`, we will
call the appropriate django-agent-trust APIs automatically. If the trust option
is selected, the agent will be trusted persistently; if not, it will be trusted
for the current session. Views willing to accept a trusted agent in lieu of OTP
verification may then use
:func:`~django_agent_trust.decorators.trusted_agent_required` in place of
:func:`~django_otp.decorators.otp_required`.
"""
from __future__ import absolute_import, division, print_function, unicode_literals

from django import forms

import django_otp.forms


class OTPAgentFormMixin(object):
    def clean_agent(self):
        user = self.get_user()

        if getattr(user, 'otp_device', None) is not None:
            if self.cleaned_data.get('otp_trust_agent'):
                user.otp_trust_this_agent = True
            else:
                user.otp_trust_this_session = True


class OTPAuthenticationForm(django_otp.forms.OTPAuthenticationForm, OTPAgentFormMixin):
    """
    Extends :class:`~django_otp.forms.OTPAuthenticationForm` with support for
    agent trust.
    """
    otp_trust_agent = forms.BooleanField(required=False, label="Trust this agent")

    def clean(self):
        cleaned_data = super(OTPAuthenticationForm, self).clean()
        self.clean_agent()

        return cleaned_data


class OTPTokenForm(django_otp.forms.OTPTokenForm, OTPAgentFormMixin):
    """
    Extends :class:`~django_otp.forms.OTPTokenForm` with support for agent
    trust.
    """
    otp_trust_agent = forms.BooleanField(required=False, label="Trust this agent")

    def clean(self):
        cleaned_data = super(OTPTokenForm, self).clean()
        self.clean_agent()

        return cleaned_data
