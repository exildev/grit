from django.db import models
from binary import ByteAField

class Validable(models.Model):
	activo = models.BooleanField(default=False)
	identificador = models.CharField(max_length=45,null=True,default=None)
	class_name = models.CharField(max_length=45, null=True,default=None)
	class Meta:
		verbose_name = "Validable"
		verbose_name_plural = "Validables"
	#end cladd

	def __unicode__(self):
		return unicode(self.activo)
	#end def
#end class

class Template(models.Model):
	template = ByteAField()
	validable = models.OneToOneField(Validable)
	
	class Meta:
		verbose_name = "Template"
		verbose_name_plural = "Templates"
	#end class

	def __unicode__(self):
		return unicode(self.validable)
	#end def
#end class
