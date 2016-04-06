"""commerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
"""from django.conf.urls import url, include
from django.contrib import admin"""
from django.conf.urls import patterns, include, url
from django.contrib import admin


from icommerce.views import *


urlpatterns = [
    #url(r'^user/(\w+)/$', userpage),
    #url(r'^$', mainpage, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^icommerce/', include('icommerce.urls', namespace='icommerce')),
]
"""from django.conf import settings
from django.conf.urls import patterns

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, }),
        )"""