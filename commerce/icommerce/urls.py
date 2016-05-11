from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic.base import RedirectView
from views import *
from models import Botiga
urlpatterns = patterns('',
    # Home page
    url(r'^$',
       RedirectView.as_view(url=reverse_lazy('icommerce:botiga_list', kwargs={'extension': 'html'})),
        name='home_page'),

    #BOTIGA
    # List Botigas: /icommerce/botigas.json
    url(r'^botigas\.(?P<extension>(json|xml|html))$',BotigaList.as_view(), name='botiga_list'),

    # Botiga details, ex.:/icommerce/botigas/id.json
    url(r'^botigas/(?P<pk>\d+)\.(?P<extension>(json|xml|html))$',BotigaDetail.as_view(), name='botiga_detail'),

    # Crea una botiga , /icommerce/botigas/create/
    url(r'^botigas/create/$', BotigaCreate.as_view(), name='botiga_create'),


    #CIUTAT
    #ciutat list, ex.: /icommerce/ciutats.json
    url(r'^ciutats\.(?P<extension>(json|xml))$', CiutatList.as_view(),name='ciutat_list'),

    #ciutat details, ex.:  /icommerce/ciutats/id.json
    url(r'^ciutats/(?P<pk>\d+)\.(?P<extension>(json|xml|html))$',CiutatDetail.as_view(),
        name='ciutat_detail'),
    # Crea una ciutat , /icommerce/botigas/create/
    url(r'^ciutats/create/$', CiutatCreate.as_view(), name='ciutat_create'),


    #MARCA
    # marca list, ex.: /icommerce/marcas/id.json
    url(r'^marcas\.(?P<extension>(json|xml))$', MarcaList.as_view(),name='marca_list'),
    # marca details, ex.:  /icommerce/marcas/id.json
    url(r'^marcas/(?P<pk>\d+)\.(?P<extension>(json|xml|html))$',MarcaDetail.as_view(),
        name='marca_detail'),
    # Crea una marca , ex.: /icommerce/marcas/create/
    url(r'^marcas/create/$', MarcaCreate.as_view(),name='marca_create'),


    #PESA
    #pesa list, ex; /icommerce/pesas.json
    url(r'^pesas\.(?P<extension>(json|xml))$', PesaRobaList.as_view(),name='pesa_list'),

    #pesa details, ex.: /icommerce/pesas/id.json
    url(r'^pesas/(?P<pk>\d+)\.(?P<extension>(json|xml|html))$',
        PesaRobaDetail.as_view(),name='pesa_detail'),

    # Crea una pesa , ex.: /icommerce/pesas/create/
    url(r'^pesas/create/$', PesaCreate.as_view(), name='pesa_create'),
)


