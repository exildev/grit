from exile_ui.admin import admin_site
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

admin_site.register(models.Criticidad)
admin_site.register(models.ElementoProteger)
admin_site.register(models.CargoRiesgo)
admin_site.register(models.Riesgo)
admin_site.register(models.EvaluacionRiesgos)
admin_site.register(models.EvaluacionEmpresa, EvaluacionEmpresaAdmin)
