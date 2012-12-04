from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

def twitter_login():
    """ Vista para el login con twitter """
    return render_to_response(
        'authentication/twitter_login.html', {},
        context_instance=RequestContext(request)
    )

