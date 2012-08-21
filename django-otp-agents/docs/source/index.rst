django-otp-agents
=================

.. include:: ../../README


Installation
------------

This is technically a Django app, but only for testing purposes. To use this
project, just make sure you have django-otp and django-agent-trust installed
correctly.


Forms
-----

.. automodule:: otp_agents.forms
    :members:


Views
-----

.. automodule:: otp_agents.views
    :members:


Decorators
----------

If you use any OTP-aware authentication forms that are *not*
trusted-agent-aware, then the following decorator may be useful. For example,
suppose you have one view protected by
:func:`~django_otp.decorators.otp_required` and another that is protected by
:func:`~django_agent_trust.decorators.trusted_agent_required`. If an
authenticated user visits the first view, he will be asked to provide an OTP
token via the standard :class:`~django_otp.forms.OTPTokenForm`, which will
verify the user, but will not set up a trusted agent. If he then visits the
second view, he will be asked to verify again, this time with the
trusted-agent-aware :class:`~otp_agents.forms.OTPTokenForm`. This is clearly not
what you intend, since OTP verification should be more than sufficient to
authorize the user for the second view.

To get around this, the following decorator effectively merges
:func:`~django_otp.decorators.otp_required` and
:func:`~django_agent_trust.decorators.trusted_agent_required` into a single
decorator that will be satisfied with either a verified user or a trusted agent.
The default behavior is to act exactly like
:func:`~django_otp.decorators.otp_required`; Pass ``accept_trusted_agent=True``
to enable the more lenient policy.

.. automodule:: otp_agents.decorators
    :members:


Changes
-------

:doc:`changes`


License
-------

.. include:: ../../LICENSE
