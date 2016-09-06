from django.db import models
from formulario.models import Formulario

class Norma(models.Model):
    nombre  = models.CharField(max_length=50)
    edicion = models.CharField(max_length=50)
    fecha_edicion = models.DateField()
    referencia    = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        return u'%s' % (self.nombre, )
    #end def
#end class

class Item(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    norma = models.ForeignKey(Norma)

    def __unicode__(self):
        return u'%s' % (self.nombre, )
    #end def
#end class

class Formato(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    item = models.ForeignKey(Item)
    documento = models.FileField(upload_to="formatos", null=True, blank=True)
    ejemplo = models.FileField(upload_to="formatos_ejemplo", null=True, blank=True)
    formulario_digital = models.OneToOneField(Formulario, null=True, blank=True)

    def __unicode__(self):
        return u'%s' % (self.nombre, )
    #end def
#end class
