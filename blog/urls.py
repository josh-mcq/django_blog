from django.conf.urls import patterns, url
from django.views.generic import ListView, DetailView
from blog.models import Post


urlpatterns = patterns('',
    # Index
    url(r'^$', 'blog.views.index'),
    
    url(
        r'^blog/view/(?P<slug>[^\.]+).html', 
        'djangorocks.blog.views.view_post', 
        name='view_blog_post'),
    url(
        r'^blog/category/(?P<slug>[^\.]+).html', 
        'djangorocks.blog.views.view_category', 
        name='view_blog_category'),


    url(r'^/category/(?P<slug>[^\.]+)', ListView.as_view(
        model=Post,
        paginate_by=5,
        )),

    # Individual posts
    url(r'^(?P<slug>[^\.]+)', DetailView.as_view(
        model=Post,
        )),
)
