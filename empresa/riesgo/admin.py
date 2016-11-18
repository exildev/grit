from exileui.admin import exileui
from django.contrib import admin
import models
import forms

class EvaluacionRiesgosInline(admin.TabularInline):
	model = models.EvaluacionRiesgos
	form =  forms.EvaluacionRiesgosForm
	extra = 0
# end class

class EvaluacionEmpresaAdmin(admin.ModelAdmin):
	inlines = [EvaluacionRiesgosInline]
	form = forms.EvaluacionEmpresaForm
	def get_inline_instances(self, request, obj=None, *args, **kwargs):
		if obj:
			return super(EvaluacionEmpresaAdmin, self).get_inline_instances(request, obj, *args, **kwargs)
		else:
			return []
		# enbd if
	# end def
# end class

exileui.register(models.Criticidad)
exileui.register(models.ElementoProteger)
exileui.register(models.CargoRiesgo)
exileui.register(models.Riesgo)
exileui.register(models.EvaluacionRiesgos)
exileui.register(models.EvaluacionEmpresa, EvaluacionEmpresaAdmin)
