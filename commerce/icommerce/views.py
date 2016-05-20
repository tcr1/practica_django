from django.contrib.auth.models import User
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
from serializers import *
from django.shortcuts import get_object_or_404, render_to_response,render
from rest_framework import generics, permissions
from django.core.urlresolvers import reverse

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

    @method_decorator(login_required(login_url="/login/"))
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

    def delete(self, request, *args, **kwargs):
        self.model.objects.filter(id=kwargs['pk']).delete()
        if self.model.__name__ == "BotigaReview":
            return HttpResponseRedirect('/icommerce/botigas/'+kwargs['pkr']+'.html')
        elif self.model.__name__ == "Botiga":
            return HttpResponseRedirect('/icommerce/botigas.html')
        elif self.model.__name__ == "Pesa":
            return HttpResponseRedirect('/icommerce/botigas.html')
        elif self.model.__name__ == "Marca":
            return HttpResponseRedirect('/icommerce/botigas.html')
        elif self.model.__name__ == "Ciutat":
            return HttpResponseRedirect('/icommerce/botigas.html')
        else:
            return HttpResponseRedirect('/')

#-------------Botiga-------------------
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
        context['RATING_CHOICES'] = Review.RATING_CHOICES
        context['average'] = self.get_average_rating()
        return context

    def get_average_rating(self):
        total = 0
        reviews = self.get_reviews()
        for rev in reviews:
            total += rev.rating

        if (len(reviews)) != 0:
            av = total / float(len(reviews))
            dec = float("{0:.2f}".format(av))
            return dec
        else:
            return 2.5

    def get_reviews(self):
        return BotigaReview.objects.filter(botiga_id=self.kwargs['pk'])

class BotigaCreate(LoginRequiredMixin, CreateView):
    model = Botiga
    template_name = 'icommerce/form.html'
    form_class = BotigaForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BotigaCreate, self).form_valid(form)

#-------------------Marca---------------------

class MarcaList(ListView, ConnegResponseMixin):
    model = Marca
    queryset = Marca.objects.all()

class MarcaDetail(DetailView, ConnegResponseMixin):
    model = Marca
    template_name = 'icommerce/Marca_detail.html'

    def get_context_data(self, **kwargs):
        context = super(MarcaDetail, self).get_context_data(**kwargs)
        return context

class MarcaCreate(LoginRequiredMixin,CreateView):
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

#---------------------Pesa-----------------------

class PesaRobaList(ListView, ConnegResponseMixin):
    model = Pesa
    queryset = Pesa.objects.all()

    def get_queryset(self):
        peces = Pesa.objects.filter(botigas=self.kwargs['pkb'])

        return peces

class PesaRobaDetail(DetailView, ConnegResponseMixin):
    model = Pesa
    template_name = 'icommerce/Pesa_Detail.html'

    def get_context_data(self, **kwargs):
        context = super(PesaRobaDetail, self).get_context_data(**kwargs)
        return context

class PesaCreate(LoginRequiredMixin,CreateView):
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

#--------------------Ciutat--------------------

class CiutatList(ListView, ConnegResponseMixin):
    model = Ciutat
    template_name = 'icommerce/Ciutat_list.html'

    def get_queryset(self):
        ciutats = Ciutat.objects.all()
        return ciutats

class CiutatDetail(DetailView, ConnegResponseMixin):
    model = Ciutat
    template_name = 'icommerce/Ciutat_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CiutatDetail, self).get_context_data(**kwargs)
        return context

class CiutatCreate(LoginRequiredMixin,CreateView):
    model = Ciutat
    template_name = 'icommerce/form.html'
    form_class = CiutatForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CiutatCreate, self).form_valid(form)

#------------------Review-------------------
@login_required()
def review(request, pk):
    botiga = get_object_or_404(Botiga, pk=pk)
    review = BotigaReview(
        rating=request.POST['rating'],
        comment=request.POST['comment'],
        user=request.user,
        botiga=botiga)
    review.save()
    return HttpResponseRedirect(reverse('icommerce:botiga_detail', args=(botiga.id,"html")))

#------------------APIRESTful-----------------------

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user

class APIBotigaList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Botiga
    queryset = Botiga.objects.all()
    serializer_class = BotigaSerializer

class APIBotigaDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Botiga
    queryset = Botiga.objects.all()
    serializer_class = BotigaSerializer

class APIMarcaList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Marca
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class APIMarcaDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Marca
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class APICiutatList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Ciutat
    queryset = Ciutat.objects.all()
    serializer_class = CiutatSerializer

class APICiutatDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Ciutat
    queryset = Ciutat.objects.all()
    serializer_class = CiutatSerializer

class APIPesaList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Pesa
    queryset = Pesa.objects.all()
    serializer_class = PesaSerializer

class APIPesaDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Pesa
    queryset = Pesa.objects.all()
    serializer_class = PesaSerializer

class APIBotigaReviewList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = BotigaReview
    queryset = BotigaReview.objects.all()
    serializer_class = BotigaReviewSerializer

class APIBotigaReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = BotigaReview
    queryset = BotigaReview.objects.all()
    serializer_class = BotigaReviewSerializer

class APIUserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    model = User
    serializer_class = UserSerializer

class APIUserDetail(generics.RetrieveUpdateDestroyAPIView):
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer


