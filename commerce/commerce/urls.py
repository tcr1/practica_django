from django.conf.urls import patterns, include, url
from icommerce.views import *
from django.contrib import admin
admin.autodiscover()




urlpatterns = patterns('',

    url(r'^$', mainpage, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout', kwargs={'next_page': '/'}),
    url(r'^icommerce/', include('icommerce.urls', namespace='icommerce')),

)
