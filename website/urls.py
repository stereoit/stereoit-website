from django.conf.urls import patterns, url, include
from django.conf import settings
from django.contrib import admin

from django.views.generic import TemplateView


from stereoit.djangoapps import news
from stereoit.djangoapps.tagcloud.models import Tag, TagCloud


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Example:
    # (r'^website/', include('website.foo.urls')),
        (r'^$', TemplateView.as_view(template_name='index.html')),

	(r'^news/', include('stereoit.djangoapps.news.urls')),
	(r'^tag-cloud$', TemplateView.as_view(template_name='tagcloud.html')),
	(r'^tags/', include('stereoit.djangoapps.tagcloud.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

if settings.LOCAL_DEVELOPMENT:
	urlpatterns += patterns('django.views', 
		(r'^static/(?P<path>.*)$', 'static.serve', {'document_root': settings.MEDIA_ROOT}),
	)
	
