from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from restaurant.models import Restaurant



def index(request):
    restaurants = Restaurant.objects.all()

    return render_to_response(
        'principal/index.html',
        {restaurants: restaurants},
        context_instance=RequestContext(request)
    )
