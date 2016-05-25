from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'blog.views.index', name='index'),
    #url(r'^blog/(?P<pk>\d+)/$', 'blog.views.index', name='post_list'),
    url(r'^blog/(?P<pk>\d+)/$', 'blog.views.post_detail', name='post_detail'),
    #url(r'^blog/(?P<pk>\d+)/edit$', 'blog.views.post_edit', name='post_edit'),
    url(r'^new/$', 'blog.views.post_new'),
]