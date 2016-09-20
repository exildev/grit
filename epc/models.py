from __future__ import unicode_literals

from django.db import models


class Contratista(models.Model):
	nombre = models.CharField(max_length=100)
# end class

class Material(models.Model):
	nombre = models.CharField(max_length=100)
# end class

class Actividad(models.Model):
	nombre = models.CharField(max_length=100)
# end class

class Proyecto(models.Model):
	nombre = models.CharField(max_length=100)
# end class


