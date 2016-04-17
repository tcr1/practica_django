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

    # List Botigas: /icommerce/botigas.json
    url(r'^botigas\.(?P<extension>(json|xml|html))$',BotigaList.as_view(), name='botiga_list'),

    # Botiga details, ex.:     /icommerce/botigas/1.json
    url(r'^botigas/(?P<pk>\d+)\.(?P<extension>(json|xml|html))$',BotigaDetail.as_view(), name='botiga_detail'),

    # Botiga marca list, ex.: /icommerce/botigas/1/marcas.json
    url(r'^botigas/(?P<pkb>\d+)/marcas\.(?P<extension>(json|xml))$',MarcaList.as_view(),name='marca_list'),

    # Botiga marca details, ex.:  /icommerce/botigas/1/marcas/1.json
    url(r'^botigas/(?P<pkb>\d+)/marcas/(?P<pk>\d+)\.(?P<extension>(json|xml|html))$',MarcaDetail.as_view(),
        name='marca_detail'),

    #Botiga marca pesa list, ex; /icommerce/botigas/1/marcas/1/pesas.json
    url(r'^botigas/(?P<pkb>\d+)/pesas\.(?P<extension>(json|xml))$', PesaRobaList.as_view(),
        name='pesa_list'),

    #Botiga marca pesa details, ex.:     /icommerce/botigas/1/marcas/1/pesas/1.json
    url(r'^botigas/(?P<pkb>\d+)/pesas/(?P<pk>\d+)\.(?P<extension>(json|xml|html))$',
        PesaRobaDetail.as_view(),name='pesa_detail'),
)


