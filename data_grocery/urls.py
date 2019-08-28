from django.conf.urls import include, url, patterns
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'groceries.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/','gtracker.views.home', name='home'),
    url(r'^gtracker/',include('gtracker.url')),
)
