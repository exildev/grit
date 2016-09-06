from django.db import models
from datetime import datetime, timedelta
from empresa.models import Empresa, Cargo, Empleado
from norma.models import Formato
from django.db.models import Q

class Recordatorio(models.Model):
	fecha = models.DateTimeField(auto_now_add=True)
	url   = models.CharField(max_length=120)
	titulo = models.CharField(max_length=45)
	cargo = models.ForeignKey(Cargo)
	dias_aviso = models.IntegerField()
	formato = models.ForeignKey(Formato)

	def __unicode__(self):
		return u'%s' % (self.titulo, )
	#end def
#end class

class Periodicidad(models.Model):
	TIPOS = (
		('Al dia', 1),
		('Cada intervalo', 2)
	)
	tipo = models.IntegerField(choices=TIPOS)
	recordatorio = models.ForeignKey(Recordatorio)
	dia = models.IntegerField(null=True, blank=True)
	mese = models.IntegerField(null=True, blank=True)
	anio = models.IntegerField(null=True, blank=True)
#end class

class Aviso(models.Model):
	fecha_aviso  = models.DateField(auto_now_add=True)
	fecha_limite = models.DateField()
	empleado = models.ForeignKey(Empleado)
	recordatorio = models.ForeignKey(Recordatorio)

	def __unicode__(self):
		return u'%s: recuerde que tiene plazo hasta el %s para %s' % (str(self.fecha_aviso), str(self.fecha_limite), str(self.recordatorio),)
	#end def

#end class

class Revision(models.Model):
	fecha = models.DateTimeField(auto_now_add=True)
	aviso = models.ForeignKey(Aviso)

#end class


