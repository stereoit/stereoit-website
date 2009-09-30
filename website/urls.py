from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^website/', include('website.foo.urls')),
	(r'^$', direct_to_template, {'template':'index2.html'}),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)

if settings.LOCAL_DEVELOPMENT:
	urlpatterns += patterns('django.views', 
		(r'^static/(?P<path>.*)$', 'static.serve', {'document_root': settings.MEDIA_ROOT}),
	)
