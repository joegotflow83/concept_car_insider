from django.conf.urls import url, patterns

from blog import views


urlpatterns = patterns(
	'blog.views',
	url(r'^$', views.blog, name='blog'),
)