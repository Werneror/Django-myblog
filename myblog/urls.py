from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.views import homepage, show_article, show_class
from comments.views import comment_app
from about.views import about
import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^66666/', include(admin.site.urls)),
    url(r'^$', homepage),
    url(r'^article/(\w+)$', show_article),
    url(r'^class/(\w+)$', show_class),
    url(r'^about$', about),
    url(r'^comments/app$', comment_app),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDAIN_PATH}
    ),
)
