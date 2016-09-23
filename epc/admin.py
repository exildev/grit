# -*- encoding: utf8 -*-
from exile_ui.admin import admin_site
from django.contrib import admin
import models
import forms

class GanttInline(admin.StackedInline):
	model = models.Gantt
	form = forms.GanttForm
	extra = 0
# end class

class ProgresoGraficoInline(admin.StackedInline):
	model = models.ProgresoGrafico
	form = forms.ProgresoGraficoForm
	extra = 0
# end class

class AdquisiscionMaterialInline(admin.StackedInline):
	model = models.AdquisiscionMaterial
	extra = 0
# end class

class ActividadInline(admin.StackedInline):
	model = models.Actividad
	form = forms.ActividadForm
	readonly_fields = ['fecha_completado', 'desface']
	extra = 0
# end class

class OrdenTrabajoAdmin(admin.ModelAdmin):
	inlines = [AdquisiscionMaterialInline, ActividadInline, ProgresoGraficoInline]
	readonly_fields = ['fecha_creacion']
# end class

class OrdenTrabajoInline(admin.StackedInline):
	model = models.OrdenTrabajo
	readonly_fields = ['fecha', 'fecha_final_estimada', 'fecha_final_real', ]
	extra = 0
# end class

class ProyectoAdmin(admin.ModelAdmin):
	inlines = [OrdenTrabajoInline, GanttInline]
# end class

admin_site.register(models.Contratista)
admin_site.register(models.Contrato)
admin_site.register(models.TipoAdquisiscion)
admin_site.register(models.Material)
admin_site.register(models.OrdenTrabajo, OrdenTrabajoAdmin)
admin_site.register(models.Actividad)
admin_site.register(models.Proyecto, ProyectoAdmin)
admin_site.register(models.ProgresoGrafico)
