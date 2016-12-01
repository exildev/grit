from exileui.admin import exileui
from django.contrib import admin
import unicodedata
import models
import forms

class CampoInline(admin.TabularInline):
	model = models.Campo
	form = forms.CampoForm
# end class

class RevisionInline(admin.StackedInline):
	model = models.Revision
	form = forms.CampoForm
	extra = 1
# end class

class FormularioAdmin(admin.ModelAdmin):
	search_fields = ('nombre', 'fecha')
	list_filter = ('fecha', )
	list_display = ('nombre', 'fecha')
	model=models.Formulario
	form = forms.FormularioForm
	inlines = [CampoInline]
#end class

class RegistroAdmin(admin.ModelAdmin):
	inlines = [RevisionInline]
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
		elif obj and obj.completado:
			self.form = forms.RegistroEditForm.make(obj)
		else:
			self.form = forms.RegistroCreateForm
		#end if
		return self.form
	#end def
#end class


exileui.register(models.Tipo)
#exileui.register(models.Campo)
exileui.register(models.Formulario, FormularioAdmin)
#exileui.register(models.Valor)
#exileui.register(models.Entrada)
exileui.register(models.Registro, RegistroAdmin)
