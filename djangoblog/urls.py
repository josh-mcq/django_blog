from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_tutorial_blog_ng.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^mcq$', 'blog.views.home', name='mcq'), #how can i get it to point to my own folder and run? a view?
    # Blog URLs
    url(r'', include('blog.urls'))

)