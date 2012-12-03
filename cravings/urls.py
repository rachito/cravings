from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    #Django
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

    #authentication
    url(r'^login/?$', 'authentication.views.twitter_login'),

    #Aplicacion Principal
    url(r'^$', 'principal.views.index'),


)
