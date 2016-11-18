from __future__ import unicode_literals
from django.db import models
from empresa.models import Empleado
from datetime import date, timedelta
from django.db.models import Sum
from adminsortable.models import SortableMixin
from norma.formulario import models as formulario

class Personal(models.Model):
	nombre = models.CharField(max_length=100)
	empleado = models.ForeignKey(Empleado, blank=True, null=True)

	def __unicode__(self):
		return "%s" % (self.nombre, )
	# end def
# end class

class Material(models.Model):
	nombre = models.CharField(max_length=100)
	uso_unico = models.BooleanField(default=False)

	def __unicode__(self):
		return "%s" % (self.nombre, )
	# end def
# end class

class TipoAdquisiscion(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return "%s" % (self.nombre, )
	# end def
# end class

class AdquisiscionMaterial(models.Model):
	material = models.ForeignKey(Material)
	orden = models.ForeignKey('OrdenTrabajo')
	tipo = models.ForeignKey(TipoAdquisiscion)
	precio = models.DecimalField(max_digits=15, decimal_places=2)
# end class

class Grupo(models.Model):
	nombre = models.CharField(max_length=100)
	def __unicode__(self):
		return "%s" % (self.nombre, )
	# end def
# end class
	
class Invitacion(models.Model):
	grupo = models.ForeignKey(Grupo)
	personal = models.ForeignKey(Personal)
# end class
	

class Proyecto(models.Model):
	nombre = models.CharField(max_length=100)
	grupo = models.ForeignKey(Grupo, null=True)
	def __unicode__(self):
		return "%s" % (self.nombre, )
	# end def
# end class

class OrdenTrabajo(models.Model):
	nombre_corto = models.CharField(max_length=45)
	proyecto = models.ForeignKey(Proyecto)
	personal = models.ForeignKey(Personal)
	revisor = models.ForeignKey(Personal, related_name="revisor")
	materiales = models.ManyToManyField(Material, through=AdquisiscionMaterial)
	fecha = models.DateField()
	fecha_creacion = models.DateField(auto_now_add=True)
	dependencias = models.ManyToManyField('OrdenTrabajo', blank=True)

	def fecha_final_estimada(self):
		act = Actividad.objects.filter(orden = self).order_by('poscicion').last()
		return act.fecha_estimada()
	# e nd def

	def fecha_final_real(self):
		act = Actividad.objects.filter(orden = self).order_by('fecha_completado').last()
		return act.fecha_completado
	# e nd def

	def completado(self):
		acts = Actividad.objects.filter(orden = self)
		if acts.filter(completado=True).count():
			print acts.count(), acts.filter(completado=True).count()
			return 100*acts.filter(completado=True).count()/acts.count()
		# end if
		return 0
	# end def
	def __unicode__(self):
		return "%s" % (self.nombre_corto, )
	# end def
# end class

class Actividad(models.Model):
	nombre = models.CharField(max_length=100)
	orden = models.ForeignKey(OrdenTrabajo)
	completado = models.BooleanField()
	dias_estimados = models.IntegerField()
	poscicion = models.PositiveIntegerField(default=0, db_index=True)
	fecha_completado = models.DateField(null=True, blank=True)
	formato = models.ForeignKey(formulario.Formulario, blank=True, null=True)
	registro = models.ForeignKey(formulario.Registro, blank=True, null=True)


	def desface(self):
		if self.fecha_completado and self.fecha_estimada():
			return self.fecha_completado - self.fecha_estimada()
		# end def
	# end def

	def fecha_estimada(self):
		acts = Actividad.objects.filter(poscicion__lte = self.poscicion, orden = self.orden).aggregate(dias=Sum('dias_estimados'))
		return self.orden.fecha+timedelta(days=acts['dias'] or 0)
	# end def

	def __unicode__(self):
		return "%s" % (self.nombre, )
	# end def

# end class

class ProgresoGrafico(models.Model):
	orden = models.OneToOneField(OrdenTrabajo)
# end class

class Gantt(models.Model):
	proyecto = models.OneToOneField(Proyecto)
# end class


