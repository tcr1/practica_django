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

    # List restaurants: /myrestaurants/restaurants.json
    url(r'^botigas\.(?P<extension>(json|xml|html))$',BotigaList.as_view(), name='botiga_list'),

    # Restaurant details, ex.: /myrestaurants/restaurants/1.json
    url(r'^botigas/(?P<pk>\d+)\.(?P<extension>(json|xml|html))$',BotigaDetail.as_view(), name='botiga_detail'),

    # Create a restaurant: /myrestaurants/restaurants/create/ #petaaa
    url(r'^botigas/create/$', BotigaCreate.as_view(), name='botiga_create'),

    # Botiga marca list, ex.: /icommerce/botigas/1/marcas.json #petaaa
    url(r'^botigas/(?P<pk>\d+)/marcas\.(?P<extension>(json|xml|html))$',MarcaList.as_view(),name='marca_list'),

    # Restaurant dish details, ex.: /myrestaurants/restaurants/1/dishes/1.json
    url(r'^botigas/(?P<pkr>\d+)/marcas/(?P<pk>\d+)\.(?P<extension>(json|xml|html))$',MarcaDetail.as_view(),
        name='marca_detail'),

    # Create a restaurant dish, ex: /myrestaurants/restaurants/1/dishes/create/ #petaaa
    url(r'^botigas/(?P<pk>\d+)/marcas/create/$',MarcaCreate.as_view(),name='marca_create'),

    #Botiga marca pesa_roba list, ex; /icommerce/botigas/1/marcas/1/pesa_robas.json
    url(r'^botigas/(?P<pk>\d+)/marcas/(?P<pk>\d+)/pesa_robas\.(?P<extension>(json|xml))$', PesaRobaList.as_view(),
        name='pesa_roba_list'),
)


