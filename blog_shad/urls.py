from django.conf.urls import url, include

from . import views


urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^$', views.articles),
    url(r'^article/(?P<article_id>\d+)/$', views.article),
    url(r'^articles/addLike/(?P<article_id>\d+)/$', views.addlike),
    url(r'^articles/addcomment/(?P<article_id>\d+)/$', views.addcomment),
    url(r'^contacts/', views.contacts),
    ]