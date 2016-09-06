# -*- encoding: utf-8 -*-
from django.db import models
from binary import ByteAField
from usr import models as usr

class Tipo(models.Model):
	FORMAS = (
		(0, 'Binario'),
		(1, 'Decimal'),
		(2, 'Entero' ),
		(3, 'Cadena' ),
		(4, 'Parrafo'),
		(5, 'Fecha'  ),
		(6, 'Hora'   ),
		(7, 'Fecha/Hora'),
	)
	forma   = models.IntegerField(choices=FORMAS)
	nombre  = models.CharField(max_length=45)
	regular = models.CharField(max_length=100, null=True, blank=True)

	def __unicode__(self):
		return u'%s' % (self.nombre, )
	#en class
#end class


class Formulario(models.Model):
	nombre = models.CharField(max_length=45)
	fecha  = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return u'%s' % (self.nombre, )
	#en class
#end class

class Campo(models.Model):
	nombre = models.CharField(max_length=45)
	tipo   = models.ForeignKey(Tipo)
	formulario = models.ForeignKey(Formulario)

	def __unicode__(self):
		return u'%s' % (self.nombre, )
	#en class
#end class

class Registro(models.Model):
	formulario = models.ForeignKey(Formulario)
	empleado = models.ForeignKey(usr.Empleado)
	completado = models.BooleanField(default=False, blank=True)
	fecha = models.DateTimeField(null=True, blank=True)
#end class

class Valor(models.Model):
	tipo  = models.ForeignKey(Tipo)
	valor = ByteAField()
	
	def __unicode__(self):
		return str(self.valor).decode('utf-8')
	#end def
#end class

class Entrada(models.Model):
	campo = models.ForeignKey(Campo)
	valor = models.ForeignKey(Valor, null=True)
	registro = models.ForeignKey(Registro)
#end class