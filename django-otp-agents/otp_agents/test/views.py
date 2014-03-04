import pickle

from django.http import HttpResponse

from otp_agents.decorators import otp_required


@otp_required
def otp_view(request):
    return HttpResponse()


@otp_required()
def otp_view_2(request):
    return HttpResponse()


@otp_required()
def pickle_view(request):
    """ Make sure the middleware didn't break pickling. """
    pickle.dumps(request.user, pickle.HIGHEST_PROTOCOL)

    return HttpResponse()


@otp_required(if_configured=True, accept_trusted_agent=True)
def otp_advised_view(request):
    return HttpResponse()


@otp_required(if_configured=True)
def otp_advised_view_2(request):
    return HttpResponse()


@otp_required(accept_trusted_agent=True)
def agent_view(request):
    return HttpResponse()
