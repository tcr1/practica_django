from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.utils import timezone
from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateResponseMixin
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.template.loader import get_template
from django.template import Context
from forms import *

#from rest_framework import generics, permissions

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

class LoginRequiredMixin(object):

    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)

class CheckIsOwnerMixin(object):
    def get_object(self, *args, **kwargs):
        obj = super(CheckIsOwnerMixin, self).get_object(*args, **kwargs)
        if not obj.user == self.request.user:
            raise PermissionDenied
        return obj

class LoginRequiredCheckIsOwnerUpdateView(LoginRequiredMixin, CheckIsOwnerMixin, UpdateView):
    template_name = 'icommerce/form.html'

class LoginRequiredCheckIsOwnerDeleteView(LoginRequiredMixin, CheckIsOwnerMixin, DeleteView):
    template_name = 'icommerce/delete_form.html'
    success_url = "/"

class BotigaList(ListView, ConnegResponseMixin):
    model = Botiga
    queryset = Botiga.objects.filter(date__lte=timezone.now()).order_by('date')
    context_object_name = 'latest_botiga_list'
    template_name = 'icommerce/Botiga_list.html'

class BotigaDetail(DetailView, ConnegResponseMixin):
    model = Botiga
    template_name = 'icommerce/Botiga_detail.html'

    def get_context_data(self, **kwargs):
        context = super(BotigaDetail, self).get_context_data(**kwargs)
        return context

class BotigaCreate(CreateView):
    model = Botiga
    template_name = 'icommerce/form.html'
    form_class = BotigaForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BotigaCreate, self).form_valid(form)

class MarcaList(ListView, ConnegResponseMixin):
    model = Marca
    queryset = Marca.objects.all()

class MarcaDetail(DetailView, ConnegResponseMixin):
    model = Marca
    template_name = 'icommerce/Marca_detail.html'

    def get_context_data(self, **kwargs):
        context = super(MarcaDetail, self).get_context_data(**kwargs)
        return context

class MarcaCreate(CreateView):
    model = Marca
    template_name = 'icommerce/form.html'
    form_class = MarcaForm

    def form_valid(self, form):
        marca = form.save(commit=False)
        marca.user = self.request.user
        marca.save()
        noms_botigues = form.cleaned_data['botigas']
        for nom_botiga in noms_botigues:
            botiga = Botiga.objects.get(nom_botiga=nom_botiga)
            form.instance.botigas.add(botiga)
        return super(MarcaCreate, self).form_valid(form)


class PesaRobaList(ListView, ConnegResponseMixin):
    model = Pesa
    queryset =  Pesa.objects.all()
    #context_object_name = 'latest_pesa_list'
    #template_name = 'icommerce/Pesa_list.html'

    def get_queryset(self):
        peces = Pesa.objects.filter(botigas=self.kwargs['pkb'])
        return peces

class PesaRobaDetail(DetailView, ConnegResponseMixin):
    model = Pesa
    template_name = 'icommerce/Pesa_Detail.html'

    def get_context_data(self, **kwargs):
        context = super(PesaRobaDetail, self).get_context_data(**kwargs)
        return context


class PesaCreate(CreateView):
    model = Pesa
    template_name = 'icommerce/form.html'
    form_class = PesaForm

    def form_valid(self, form):
        pesa = form.save(commit=False)
        pesa.user = self.request.user
        pesa.save()
        noms_botigues = form.cleaned_data['botigas']
        for nom_botiga in noms_botigues:
            botiga = Botiga.objects.get(nom_botiga=nom_botiga)
            form.instance.botigas.add(botiga)
        return super(PesaCreate, self).form_valid(form)

class CiutatList(ListView, ConnegResponseMixin):
    model = Ciutat
    #queryset = Ciutat.objects.all()#filter(date__lte=timezone.now()).order_by('date')[:5]
    #context_object_name = 'latest_ciutat_list'
    template_name = 'icommerce/Ciutat_list.html'

    def get_queryset(self):
        ciutats = Ciutat.objects.all()#filter(botigas=self.kwargs['pkb'])
        return ciutats

class CiutatDetail(DetailView, ConnegResponseMixin):
    model = Ciutat
    template_name = 'icommerce/Ciutat_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CiutatDetail, self).get_context_data(**kwargs)
        return context

class CiutatCreate(CreateView):
    model = Ciutat
    template_name = 'icommerce/form.html'
    form_class = CiutatForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CiutatCreate, self).form_valid(form)

@login_required()
def review(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    review = RestaurantReview(
        rating=request.POST['rating'],
        comment=request.POST['comment'],
        user=request.user,
        restaurant=restaurant)
    review.save()
    return HttpResponseRedirect(reverse('myrestaurants:restaurant_detail', args=(restaurant.id,)))