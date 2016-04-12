from django.conf.urls import patterns, include, url
from icommerce.views import *
from django.contrib import admin
admin.autodiscover()




urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^icommerce/', include('icommerce.urls', namespace='icommerce')),
    url(r'^$', mainpage ,name='home'),
)
