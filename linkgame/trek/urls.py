from django.conf.urls.defaults import *
from django.contrib.auth.views import login, logout
from trek.views import new_game, update_points, claim_link, profile
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       (r'^$', login),
                       (r'^newgame/$', new_game),
                       (r'^accounts/login/$',  login),
                       (r'^accounts/logout/$', logout),    
                       (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
                        {'document_root': './trek/media'}),
                       (r'^newgame/addpoints/(?P<p>.*)$', update_points),
                       (r'^newgame/claim/$', claim_link),
                      # (r'^user/(?P<username>\w{1,50})/profile/$', profile),
                       (r'^user/(?P<username>.*)/$', profile),
          

    # Example:
    # (r'^linkgame/', include('linkgame.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
