from django.utils import timezone
from django.core import serializers
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.edit import CreateView

from models import Botiga
from forms import *


# Create your views here.
class ConnegResponseMixin(TemplateResponseMixin):

    def render_json_object_response(self, objects, **kwargs):
        json_data = serializers.serialize(u"json", objects, **kwargs)
        return HttpResponse(json_data, content_type=u"application/json")

    def render_xml_object_response(self, objects, **kwargs):
        xml_data = serializers.serialize(u"xml", objects, **kwargs)
        return HttpResponse(xml_data, content_type=u"application/xml")

    def render_to_response(self, context, **kwargs):
        if 'extension' in self.kwargs:
            try:
                objects = [self.object]
            except AttributeError:
                objects = self.object_list
            if self.kwargs['extension'] == 'json':
                return self.render_json_object_response(objects=objects)
            elif self.kwargs['extension'] == 'xml':
                return self.render_xml_object_response(objects=objects)
        return super(ConnegResponseMixin, self).render_to_response(context)

class BotigaCreate(CreateView):
    model = Botiga
    template_name = 'icommerce/form.html'
    form_class = BotigaForm

    def form_valid(self, form):

        form.instance.user = self.request.user
        print "hola2"
        aux = super(BotigaCreate, self)
        print "form"
        print aux.form_valid(form)
        return super(BotigaCreate, self).form_valid(form)

class BotigaList(ListView, ConnegResponseMixin):
    model = Botiga
    queryset = Botiga.objects.filter(date__lte=timezone.now()).order_by('date')[:5]
    context_object_name = 'latest_botiga_list'
    template_name = 'icommerce/Botiga_list.html'

class BotigaDetail(DetailView, ConnegResponseMixin):
    print "2"
    model = Botiga
    template_name = 'icommerce/Botiga_detail.html'

    def get_context_data(self, **kwargs):
        print "1"
        context = super(BotigaDetail, self).get_context_data(**kwargs)
        #context['RATING_CHOICES'] = RestaurantReview.RATING_CHOICES
        return context

class MarcaList(ListView, ConnegResponseMixin):
    model =Marca
    #print "hello"
    queryset =  Marca.objects.all()#filter(date__lte=timezone.now()).order_by('date')[:5]#Marca.objects.all()
    context_object_name = 'latest_marca_list'
    template_name = 'icommerce/Marca_list.html'


    def get_queryset(self):
        ## print self.kwargs['pkb']
        marques = Marca.objects.filter(botiga=self.kwargs['pkb'])
        #print marques
        return marques

class MarcaDetail(DetailView, ConnegResponseMixin):
    model = Marca
    template_name = 'icommerce/Marca_detail.html'

    def get_context_data(self, **kwargs):
        #print "1"
        context = super(MarcaDetail, self).get_context_data(**kwargs)
        #context['RATING_CHOICES'] = RestaurantReview.RATING_CHOICES
        return context

class MarcaCreate(CreateView):
    model = Marca
    template_name = 'icommerce/form.html'
    form_class = MarcaForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.botiga = Botiga.objects.get(id=self.kwargs['pkb'])
        return super(MarcaCreate, self).form_valid(form)

class PesaRobaList(ListView, ConnegResponseMixin):
    model = Pesa
    #print "hello"
    queryset =  Pesa.objects.all()#filter(date__lte=timezone.now()).order_by('date')[:5]#Marca.objects.all()
    context_object_name = 'latest_pesa_list'
    template_name = 'icommerce/Pesa_list.html'

    def get_queryset(self):
        ## print self.kwargs['pkb']
        peces = Pesa.objects.filter(botiga_pesa=self.kwargs['pkb'], marca_pesa=self.kwargs['pkm'])
        # print marques
        return peces

class PesaRobaDetail(DetailView, ConnegResponseMixin):
    model = Pesa
    template_name = 'icommerce/Pesa_detail.html'

    def get_context_data(self, **kwargs):
        # print "1"
        context = super(PesaRobaDetail, self).get_context_data(**kwargs)
        # context['RATING_CHOICES'] = RestaurantReview.RATING_CHOICES
        return context