from django.forms import ModelForm
from models import *

class BotigaForm(ModelForm):
    class Meta:
        model = Botiga
        exclude = ('user', 'date',)

class MarcaForm(ModelForm):
    class Meta:
        model = Marca
        exclude = ('user', 'date', 'botiga',)