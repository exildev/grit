from exile_ui.admin import admin_site
from django.contrib import admin
import models

class EvaluacionRiesgosInline(admin.TabularInline):
	model = models.EvaluacionRiesgos
# end class

class EvaluacionEmpresaAdmin(admin.ModelAdmin):
	inlines = [EvaluacionRiesgosInline]
# end class

admin_site.register(models.Criticidad)
admin_site.register(models.ElementoProteger)
admin_site.register(models.CargoRiesgo)
admin_site.register(models.Riesgo)
admin_site.register(models.EvaluacionRiesgos)
admin_site.register(models.EvaluacionEmpresa, EvaluacionEmpresaAdmin)
