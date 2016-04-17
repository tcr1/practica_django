from django.utils import timezone
from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateResponseMixin
from django.template.loader import get_template
from django.template import Context
from forms import *

def mainpage(request):
    template = get_template('mainpage.html')
    variables = Context({
        'titlehead': 'Icommerce Tandy',
        'pagetitle': 'Welcome to Tandy',
        'contentbody': 'A new page made in Spain since 2016',
        'user': request.user,
        'main':'true',
    })
    output = template.render(variables)
    return HttpResponse(output)

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

class BotigaList(ListView, ConnegResponseMixin):
    model = Botiga
    queryset = Botiga.objects.filter(date__lte=timezone.now()).order_by('date')[:5]
    context_object_name = 'latest_botiga_list'
    template_name = 'icommerce/Botiga_list.html'

class BotigaDetail(DetailView, ConnegResponseMixin):
    model = Botiga
    template_name = 'icommerce/Botiga_detail.html'

    def get_context_data(self, **kwargs):
        context = super(BotigaDetail, self).get_context_data(**kwargs)
        return context

class MarcaList(ListView, ConnegResponseMixin):
    model =Marca
    queryset =  Marca.objects.all()

    def get_queryset(self):
        marques = Marca.objects.filter(botiga=self.kwargs['pkb'])
        return marques

class MarcaDetail(DetailView, ConnegResponseMixin):
    model = Marca
    template_name = 'icommerce/Marca_detail.html'

    def get_context_data(self, **kwargs):
        context = super(MarcaDetail, self).get_context_data(**kwargs)
        return context

class PesaRobaList(ListView, ConnegResponseMixin):
    model = Pesa
    queryset =  Pesa.objects.all()
    context_object_name = 'latest_pesa_list'
    template_name = 'icommerce/Pesa_list.html'

    def get_queryset(self):
        peces = Pesa.objects.filter(botiga_pesa=self.kwargs['pkb'], marca_pesa=self.kwargs['pkm'])
        return peces

class PesaRobaDetail(DetailView, ConnegResponseMixin):
    model = Pesa
    template_name = 'icommerce/Pesa_Detail.html'

    def get_context_data(self, **kwargs):
        context = super(PesaRobaDetail, self).get_context_data(**kwargs)
        return context