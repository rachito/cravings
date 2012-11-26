from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from restaurant.models import Restaurant
from principal.models import UserProfile
from django.contrib.auth.models import User
from forms import UserForm, ProfileForm


def index(request):
    restaurants = Restaurant.objects.all()

    return render_to_response('principal/index.html',
        {restaurants: restaurants},
        context_instance=RequestContext(request)
    )

def edit_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        user_profile = ProfileForm(request.POST)

        if user_form.is_valid() and user_profile.is_valid():
            user_form.save()
            user_profile.save()
            return HttpResponseRedirect('edit/profile')

    else:
        user_form = UserForm(instance=request.user)
        user_profile = ProfileForm()

    return render_to_response('principal/edit_profile.html',
        {'user_form': user_form, 'user_profile': user_profile},
        context_instance=RequestContext(request)
    )