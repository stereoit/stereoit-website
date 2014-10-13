from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView
from django.views.generic.list import ListView

from stereoit.djangoapps.news.models import News


urlpatterns = patterns('stereoit.djangoapps.news.views',
#     (r'show/1/$', 'news_test'), #show news detail
	(r'^$', TemplateView.as_view(template_name='news/index.html')),
	(r'^archive/$', ListView.as_view(model=News,
				paginate_by=20,
				context_object_name='news',
			)),
    url(r'^(?P<slug>[-\w]+)$', 'detail', name="news_detail"), #show news detail
)
