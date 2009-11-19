from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.conf import settings
from django.contrib import admin

from stereoit.djangoapps import news
from stereoit.djangoapps.tagcloud.models import Tag, TagCloud


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Example:
    # (r'^website/', include('website.foo.urls')),
	(r'^$', direct_to_template, {'template':'index.html'}),

	(r'^news/', include('stereoit.djangoapps.news.urls')),
	(r'^tag-cloud$', direct_to_template, {'template':'tagcloud.html'}),
	(r'^tags/', include('stereoit.djangoapps.tagcloud.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

if settings.LOCAL_DEVELOPMENT:
	urlpatterns += patterns('django.views', 
		(r'^static/(?P<path>.*)$', 'static.serve', {'document_root': settings.MEDIA_ROOT}),
	)
	
