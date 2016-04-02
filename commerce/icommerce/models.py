from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Botiga (models.Model):
    id_botiga=models.IntegerField()
    nom_botiga=models.TextField(blank=True, null=True)
    tipus_botiga=models.TextField(blank=True, null=True)
    adreça=models.TextField(blank=True, null=True)

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('commerce:botiga_detail', kwargs={'pk': self.pk})

class Marca(models.Model):
    codi_marca = models.IntegerField()
    nom_marca = models.TextField(blank=True, null=True)
    descripcio = models.TextField(blank=True, null=True)
    botiga = models.ForeignKey(Botiga,null=True,related_name='botigues')

    def __unicode__(self):
        return u"%s" % self.name

    def get_absolute_url(self):
        return reverse('commerce:marca_detail', kwargs={'pkr': self.botiga.pk,'pk': self.pk})


class Peça_roba(models.Model):
    RATING_TIPUS = ((1,'pantalo'),(2,'jersei'),(3,'blusa'),(4,'camiseta'),(5,'jaqueta'),(6,'Roba_interior'),(7,'short'))
    tipus = models.PositiveSmallIntegerField('Rating (stars)',blank=False, default=1, tipus=RATING_TIPUS)
    RATING_COLORS = ((1,'WHITE'),(2,'PINK'),(3,'BLACK'),(4,'BLUE'),(5,'BROWN'))
    colors = models.PositiveSmallIntegerField('Rating (stars)'blank=false, default=1,colors=RATING_COLORS)
    codi_peça = models.IntegerField()
    nom = models.TextField()
    preu = models.DecimalField('Euro amount',max_digits=8,decimal_places=2,blank=True,null=True)
    descripcio = models.TextField(blank=True,null=True)
    talla = models.IntegerField()
    imatge = models.ImageField(upload_to="commerce",blank=True,null=True)

class Ciutat(models.Model):
    nom_ciutat = models.TextField()
    moneda = models.TextField(default="euro")