from django.conf.urls.defaults import *
from django.contrib import admin
from django.contrib.auth.views import login, logout

admin.autodiscover()

urlpatterns = patterns(
    '',
    
    # Django admin
    (r'^admin/(.*)', admin.site.root),
    
    # Web API (REST)
    (r'^api/', include('csc.webapi.urls')),
    
    (r'^trek/', include('linkgame.trek.urls')),

    (r'^accounts/login/$',  login),
    (r'^accounts/logout/$',  logout),
 )
    
