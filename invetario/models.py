from django.db import models
from empresa.models import Empleado

class Activo(models.Model):
	codigo = models.CharField(max_lenth=45)
	nombre = models.CharField(max_lenth=100)
	codigo_de_compra = models.CharField(max_lenth=45)
	precio = models.DecimalField(max_digits=15, decimal_place=2)
#end class 

class Ciudad(models.Model):
	nombre = models.CharField(max_lenth=45)
#end class

class Bodega(models.Model):
	codigo = models.CharField(max_lenth=45)
	nombre = models.CharField(max_lenth=100)
	ciudad = models.ForeignKey(Ciudad)
	direccion = models.CharField(max_digits=160)
	gps = models.CharField(max_digits=45)
#end class

class Existencia(models.Model):
	activo = models.ForeignKey(Activo)
	consecutivo = models.IntegerField()
	bodega = models.ForeignKey(Bodega, null=True, blank=True)
	custodio = models.ForeignKey(Empleado, null=True, blank=True)
#end class

class Encargado(models.Model):
	

class TraspasoDeCustodia(models.Model):
