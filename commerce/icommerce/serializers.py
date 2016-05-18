from django.contrib.auth.models import User
from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from models import *

class BotigaSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='icommerce:botiga-detail')
    marcas = HyperlinkedRelatedField(many=True, read_only=True, view_name='icommerce:marca-detail')
    botigareview_set = HyperlinkedRelatedField(many=True, read_only=True,view_name='icommerce:botiga-detail')
    user = CharField(read_only=True)

    class Meta:
        model = Botiga
        fields = ('uri', 'nom_botiga', 'tipus_botiga', 'user', 'date','marcas','botigareview_set')

class MarcaSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='icommerce:marca-detail')
    botigas = HyperlinkedRelatedField(many=True,view_name='icommerce:botiga-detail', read_only=True)
    user = CharField(read_only=True)

    class Meta:
        model = Marca
        fields = ('uri', 'nom_marca', 'user', 'descripcio', 'date','botigas')


class CiutatSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='icommerce:ciutat-detail')
    botiga_ciutat= HyperlinkedRelatedField(many=True, view_name='icommerce:botiga-detail', read_only=True)
    user = CharField(read_only=True)

    class Meta:
        model = Ciutat
        fields = ('uri', 'nom_ciutat', 'calle', 'moneda', 'botiga_ciutat', 'user')

class PesaSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='icommerce:pesa-detail')
    botigas = HyperlinkedRelatedField(many=True, view_name='icommerce:botiga-detail', read_only=True)
    user = CharField(read_only=True)

    class Meta:
        model = Pesa
        fields = ('uri', 'nom_pesa', 'tipus', 'colors', 'talla', 'preu', 'descripcio', 'user','botigas', 'botigas')


class BotigaReviewSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='icommerce:botigareview-detail')
    botiga = HyperlinkedRelatedField(view_name='icommerce:botiga-detail', read_only=True)
    user = CharField(read_only=True)

    class Meta:
        model = BotigaReview
        fields = ('uri', 'rating', 'comment', 'user', 'date', 'botiga')

class UserSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email')