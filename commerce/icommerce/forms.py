from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from models import *

class BotigaForm(ModelForm):
    class Meta:
        model = Botiga
        exclude = ('user', 'date',)

class MarcaForm(ModelForm):
    class Meta:
        model = Marca
        exclude = ('user', 'date',)


class UbicacioForm(ModelForm):
    class Meta:
        model = Ubicacio
        exclude = ('user', 'date',)

class PesaForm(ModelForm):
    class Meta:
        model = Pesa
        exclude = ('user', 'date',)

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        exclude = ('user', 'date',)