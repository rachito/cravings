from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from registration.forms import RegistrationFormUniqueEmail

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),

    
    #Registration
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),

    url(r'^accounts/register/$', 'registration.views.register',
    {'form_class': RegistrationFormUniqueEmail,
     'backend': 'registration.backends.default.DefaultBackend'},       
     name='registration_register'),

    (r'^accounts/', include('registration.backends.default.urls')),



    #Principal
    url(r'^$', 'principal.views.index'),
    url(r'^edit/profile', 'principal.views.edit_profile')
    )
