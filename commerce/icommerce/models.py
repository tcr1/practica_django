
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from datetime import date
# Create your models here.

class Ciutat(models.Model):
    nom_ciutat = models.TextField()
    moneda = models.TextField(default="euro")

    def __unicode__(self):
        return u"%s" % self.nom_ciutat

    def get_absolute_url(self):
        return reverse('icommerce:ciutat_detail', kwargs={'pk': self.pk,'extension': 'html'})

class Botiga (models.Model):
    nom_botiga=models.TextField(blank=True, null=True)
    tipus_botiga=models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=1)
    adressa=models.TextField(blank=True, null=True)
    ciutat= models.ForeignKey(Ciutat, null=True, related_name='ciutats')
    date = models.DateField(default=date.today)

    def __unicode__(self):
        return u"%s" % self.nom_botiga

    def get_absolute_url(self):
        return reverse('icommerce:botiga_detail', kwargs={'pkc': self.ciutat.pk,'pk': self.pk, 'extension': 'html'})

class Marca(models.Model):
    nom_marca = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=1)
    descripcio = models.TextField(blank=True, null=True)
    #botiga = models.ForeignKey(Botiga,null=True,related_name='marcas')
    date = models.DateField(default=date.today)
    botigas = models.ManyToManyField(Botiga,null=True,related_name='marcas')

    def __unicode__(self):
        return u"%s" % self.nom_marca

    def get_absolute_url(self):
        return reverse('icommerce:marca_detail', kwargs={'pkb': self.botigas.pk,'pk': self.pk, 'extension': 'html'})


class Pesa(models.Model):
    nom_pesa = models.TextField(blank=True, null=True)
    RATING_TIPUS= ((1,'Pantalo'),(2,'Jersei'),(3,'Blusa'),(4,'Camiseta'),(5,'Jaqueta'),(6,'Roba_interior'),(7,'Short'),
                  (8,'Faldilla'),(9,'Sabates'),(10,'Complements'),(11,'Vestit'))
    tipus = models.PositiveSmallIntegerField('CATEGORIES',blank=False,choices=RATING_TIPUS)

    RATING_COLORS = ((1,'Blanc'),(2,'Negre'),(3,'Gris'),(4,'Marro'),(5,'Blau'),(6,'Verd'),(7,'Groc'),(8,'Roig'),
                     (9,'Rosa'),(10,'Lila'),(11,'Taronja'))
    colors = models.PositiveSmallIntegerField('COLORS',blank=False, default=1,choices=RATING_COLORS)
    RATING_TALLES = ((1, 'XS'), (2, 'S'), (3, 'M'), (4, 'L'), (5, 'XL'),(6,'XXL'))
    talla = models.PositiveSmallIntegerField('TALLA', blank=False, default=1, choices=RATING_TALLES)
    preu = models.DecimalField('Preu',max_digits=8,decimal_places=2,blank=True,null=True)
    descripcio = models.TextField(blank=True,null=True)
    #botiga_pesa = models.ForeignKey(Botiga, null=True, related_name='botigpesas')
    #marca_pesa = models.ForeignKey(Marca, null=True, related_name='marca')
    user = models.ForeignKey(User, default=1)
    #marcas=models.ManyToManyField(Marca)
    botigas=models.ManyToManyField(Botiga,null=True, related_name='botigpesas')

    def __unicode__(self):
        return u"%s" % self.nom_pesa

    def get_absolute_url(self):
        return reverse('icommerce:pesa_detail', kwargs={'pkb': self.botigas, """'pkm': self.marca_pesa.pk""" 'pk':self.pk,
                                                        'extension': 'html' })