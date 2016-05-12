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

    # Edit botiga details, ex.:/icommerce/botigas/id/edit
    url(r'^botigas/(?P<pk>\d+)/edit/$', LoginRequiredCheckIsOwnerUpdateView.as_view(model=Botiga,
                                                                                   form_class=BotigaForm),
        name='botiga_edit'),

    #Delete Botiga, ex:/icomerce/botigas/id/delete
    url(r'^botigas/(?P<pk>\d+)/delete/$',LoginRequiredCheckIsOwnerDeleteView.as_view(model=Botiga),name='botiga_delete'),

    #CIUTAT

    #ciutat list, ex.: /icommerce/ciutats.json
    url(r'^ciutats\.(?P<extension>(json|xml))$', CiutatList.as_view(),name='ciutat_list'),

    #ciutat details, ex.:  /icommerce/ciutats/id.json
    url(r'^ciutats/(?P<pk>\d+)\.(?P<extension>(json|xml|html))$',CiutatDetail.as_view(),
        name='ciutat_detail'),

    # Crea una ciutat , /icommerce/botigas/create/
    url(r'^ciutats/create/$', CiutatCreate.as_view(), name='ciutat_create'),

    # Edit ciutats details, ex.:/icommerce/ciutats/id/edit
    url(r'^cuitats/(?P<pk>\d+)/edit/$',LoginRequiredCheckIsOwnerUpdateView.as_view(model=Ciutat,
                                                                                   form_class=CiutatForm),
        name='ciutat_edit'),

    #Delete Ciutat, ex:/icomerce/ciutats/id/delete
    url(r'^ciutats/(?P<pk>\d+)/delete/$',LoginRequiredCheckIsOwnerDeleteView.as_view(model=Ciutat),name='ciutat_delete'),


    #MARCA

    # marca list, ex.: /icommerce/marcas/id.json
    url(r'^marcas\.(?P<extension>(json|xml))$', MarcaList.as_view(),name='marca_list'),

    # marca details, ex.:  /icommerce/marcas/id.json
    url(r'^marcas/(?P<pk>\d+)\.(?P<extension>(json|xml|html))$',MarcaDetail.as_view(),
        name='marca_detail'),

    # Crea una marca , ex.: /icommerce/marcas/create/
    url(r'^marcas/create/$', MarcaCreate.as_view(),name='marca_create'),

    # Edit marca details, ex.:/icommerce/marcas/id/edit
    url(r'^marcas/(?P<pk>\d+)/edit/$',LoginRequiredCheckIsOwnerUpdateView.as_view(model=Marca,
                                                                                  form_class=MarcaForm),
        name='marca_edit'),

    #Delete Marca, ex:/icomerce/marcas/id/delete
    url(r'^marcas/(?P<pk>\d+)/delete/$',LoginRequiredCheckIsOwnerDeleteView.as_view(model=Marca),name='marca_delete'),

    #PESA

    #pesa list, ex; /icommerce/pesas.json
    url(r'^pesas\.(?P<extension>(json|xml))$', PesaRobaList.as_view(),name='pesa_list'),

    #pesa details, ex.: /icommerce/pesas/id.json
    url(r'^pesas/(?P<pk>\d+)\.(?P<extension>(json|xml|html))$',
        PesaRobaDetail.as_view(),name='pesa_detail'),

    # Crea una pesa , ex.: /icommerce/pesas/create/
    url(r'^pesas/create/$', PesaCreate.as_view(), name='pesa_create'),

    # Edit pesa details, ex.:/icommerce/pesas/id/edit
     url(r'^pesas/(?P<pk>\d+)/edit/$',LoginRequiredCheckIsOwnerUpdateView.as_view(model=Pesa,
                                                                                  form_class=PesaForm),
         name='pesa_edit'),

    #Delete Pesa, ex:/icomerce/ciutats/id/delete
    url(r'^pesas/(?P<pk>\d+)/delete/$',LoginRequiredCheckIsOwnerDeleteView.as_view(model=Pesa),name='pesa_delete'),
)


