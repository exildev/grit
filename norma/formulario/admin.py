from huella.admin import admin_site
from django.contrib import admin
import unicodedata
import models
import forms

class CampoInline(admin.TabularInline):
	model = models.Campo
	form = forms.CampoForm

class FormularioAdmin(admin.ModelAdmin):
	search_fields = ('nombre', 'fecha')
	list_filter = ('fecha', )
	list_display = ('nombre', 'fecha')
	model=models.Formulario
	form = forms.FormularioForm
	inlines = [CampoInline]
#end class

class RegistroAdmin(admin.ModelAdmin):
	model = models.Registro
	search_fields = ('formulario__nombre', 'empleado___empleado__nombre', 'empleado___empleado__apellido', 'fecha')
	list_filter = ('formulario', 'completado', 'fecha')
	list_display = ('formulario', 'nombre_empleado', 'completado', 'fecha')
	def nombre_empleado(self, obj):
		return "%s %s" % (obj.empleado._empleado.nombre, obj.empleado._empleado.apellido)
	#end def

	def get_form(self, request, obj=None, *args, **kwargs):
		if obj and request.user.pk == obj.empleado.pk:
			self.form = forms.RegistroEditForm.make(obj)
		else:
			self.form = forms.RegistroCreateForm
		#end if
		return self.form
	#end def
#end class


admin_site.register(models.Tipo)
#admin_site.register(models.Campo)
admin_site.register(models.Formulario, FormularioAdmin)
#admin_site.register(models.Valor)
#admin_site.register(models.Entrada)
admin_site.register(models.Registro, RegistroAdmin)