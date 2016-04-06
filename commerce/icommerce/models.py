
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from datetime import date
# Create your models here.
class Botiga (models.Model):
    id_botiga=models.IntegerField()
    nom_botiga=models.TextField(blank=True, null=True)
    tipus_botiga=models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=1)
    adressa=models.TextField(blank=True, null=True)
    date = models.DateField(default=date.today)

    def __unicode__(self):
        return u"%s" % self.id_botiga #+ " " + self.nom_botiga

    def get_absolute_url(self):
        print "adeu"
        return reverse('icommerce:botiga_detail', kwargs={'pk': self.pk, 'extension': 'html'})

class Marca(models.Model):
    codi_marca = models.IntegerField()
    nom_marca = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=1)
    descripcio = models.TextField(blank=True, null=True)
    botiga = models.ForeignKey(Botiga,null=True,related_name='botigues')
    date = models.DateField(default=date.today)

    def __unicode__(self):
        return u"%s" % self.codi_marca

    def get_absolute_url(self):
        return reverse('icommerce:marca_detail', kwargs={'pkb': self.botiga.pk,'pk': self.pk, 'extension': 'html'})


class Pesa_roba(models.Model):
    codi_pesa = models.IntegerField()
    RATING_TIPUS= ((1,'Pantalo'),(2,'Jersei'),(3,'Blusa'),(4,'Camiseta'),(5,'Jaqueta'),(6,'Roba_interior'),(7,'Short'),
                  (8,'Faldilla'),(9,'Sabates'),(10,'Complements'),(11,'Vestit'))
    tipus = models.PositiveSmallIntegerField('CATEGORIES',blank=False,choices=RATING_TIPUS)
    nom = models.TextField()
    RATING_COLORS = ((1,'Blanc'),(2,'Negre'),(3,'Gris'),(4,'Marro'),(5,'Blau'),(6,'Verd'),(7,'Groc'),(8,'Roig'),(9,'Rosa'),
                     (10,'Lila'),(11,'Taronja'))
    colors = models.PositiveSmallIntegerField('COLORS',blank=False, default=1,choices=RATING_COLORS)
    RATING_TALLES = ((1, 'XS'), (2, 'S'), (3, 'M'), (4, 'L'), (5, 'XL'),(6,'XXL'))
    talla = models.PositiveSmallIntegerField('TALLA', blank=False, default=1, choices=RATING_TALLES)
    preu = models.DecimalField('Preu',max_digits=8,decimal_places=2,blank=True,null=True)
    descripcio = models.TextField(blank=True,null=True)
    imatge = models.ImageField(upload_to="icommerce",blank=True,null=True)
    user = models.ForeignKey(User, default=1)

    def __unicode__(self):
        return u"%s" % self.codi_pesa #+ " " + self.nom

    def get_absolute_url(self):
        return reverse('icommerce:Pesa_roba_detail', kwargs={'pk': self.pk})

class Ciutat(models.Model):
    nom_ciutat = models.TextField()
    moneda = models.TextField(default="euro")