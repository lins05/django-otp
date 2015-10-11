from django.contrib.auth.signals import user_logged_in

from django_agent_trust import trust_agent, trust_session


def _handle_auth_login(sender, request, user, **kwargs):
    """
    Automatically establishes agent trust if indicated by one of our
    authentication forms.
    """
    from django_agent_trust.models import AgentSettings

    AgentSettings.objects.get_or_create(user=user)

    if getattr(user, 'otp_trust_this_agent', False):
        trust_agent(request)
    elif getattr(user, 'otp_trust_this_session', False):
        trust_session(request)


user_logged_in.connect(_handle_auth_login)
