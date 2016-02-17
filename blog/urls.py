from views import homepage, show_article
from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', homepage),
    url(r'^article/(\w+)$', show_article),
)
