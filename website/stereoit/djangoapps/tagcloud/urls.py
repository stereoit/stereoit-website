from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView
from django.views.generic import TemplateView

from stereoit.djangoapps.tagcloud.models import Tag, TagCloud

tags_dict = {
	'queryset' : Tag.objects.all()
}

urlpatterns = patterns('stereoit.djangoapps.tagcloud.views',
	(r'^$', TemplateView.as_view(template_name='tagcloud/index.html')),
    url(r'ajax/description/(?P<slug>[-\w]+)/$', 'tag_tooltip_description', name="ajax-tag-description"),
    url(r'ajax/(?P<slug>[-\w]+)/$', 'tag_tooltip', name="ajax-tag"), #show tag detail
    url(r'^cloud/(?P<slug>[-\w]+)/$', 'tagcloud_detail', name="tagcloud_detail"), #show the coud detail
    url(r'(?P<slug>[-\w]+)/$', 'tag_detail', name="tag_detail"), #show tag detail
)
