# -*- coding: utf-8 -*-
from django.db import models
from empresa.models import Cargo
from empresa.models import Empresa, Cargo

class Criticidad(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField()

    def __unicode__(self):
        return u'%s' % (self.nombre, )
    #end def
#end class

class ElementoProteger(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True)

    def __unicode__(self):
        return u'%s' % (self.nombre, )
    #end def
#end class

class CargoRiesgo(models.Model):
    acceso  = models.IntegerField(default=0, blank=True, null=True)
    impacto = models.IntegerField(default=0, blank=True, null=True)
    contacto_aproteger = models.IntegerField(default=0, blank=True, null=True)
    manejo_programas   = models.IntegerField(default=0, blank=True, null=True)
    incidencia_medidas = models.IntegerField(default=0, blank=True, null=True)
    ponderacion  = models.FloatField(default=0, blank=True, null=True)
    calificacion = models.IntegerField(default=0, blank=True, null=True)
    cargo = models.OneToOneField(Cargo)
    criticidad = models.ForeignKey(Criticidad)
    aproteger  = models.ManyToManyField(ElementoProteger, blank=True)

#end class

class Riesgo(models.Model):
    amenaza = models.TextField(blank=True)
    riesgo  = models.TextField(blank=True)
    empresa = models.ForeignKey(Empresa)
    aproteger = models.ManyToManyField(ElementoProteger, blank=True)

    def __unicode__(self):
        return u'%s' % (self.riesgo, )
    #end def
#end def

class EvaluacionEmpresa(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    aprobado = models.BooleanField(default=False)
    empresa  = models.ForeignKey(Empresa)
#end class

class EvaluacionRiesgos(models.Model):
    probabilidades = (
        (1, 'Raro'),
        (2, 'Improbable'),
        (3, 'Posible'),
        (4, 'Probable'),
        (5, 'Casi seguro')
    )
    consecuencias = (
        (1, 'Insignificacnte'),
        (2, 'Menor'),
        (3, 'Moderada'),
        (4, 'Mayor'),
        (5, 'Catastrófica')
    )
    estimaciones = (
        (1, 'Bajo'),
        (2, 'Moderado'),
        (3, 'Alto'),
        (4, 'Extremo')
    )
    empresa = models.ForeignKey(EvaluacionEmpresa, null=True, blank=True)
    riesgo  = models.ForeignKey(Riesgo, null=True, blank=True)
    fuente  = models.TextField(null=True, blank=True)
    medio   = models.TextField(null=True, blank=True)
    persona = models.TextField(null=True, blank=True)
    metodo  = models.TextField(null=True, blank=True)

    probabilidad  = models.IntegerField(choices=probabilidades, null=True, blank=True)
    consecuencia  = models.IntegerField(choices=consecuencias, null=True, blank=True)

    controles_administrativos = models.TextField(null=True, blank=True)
    controles_operacionales   = models.TextField(null=True, blank=True)
    controles_talentoHumano   = models.TextField(null=True, blank=True)
    controles_instalacion     = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return u'%s' % (self.riesgo.amenaza, )
    #end def
#end class