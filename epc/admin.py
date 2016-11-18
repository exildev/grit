# -*- encoding: utf8 -*-
from exileui.admin import exileui
from exileui.admin import exileui, ExStacked, ExTabular, ExTab, DateRangeEX, DateRangeEX
from usr.models import Empleado as EmpleadoU
from cuser.middleware import CuserMiddleware
from django.contrib import admin
import nested_admin
import models
import forms


class GanttInline(ExTab):
    model = models.Gantt
    form = forms.GanttForm
    extra = 0
# end class


class ProgresoGraficoInline(nested_admin.NestedStackedInline):
    model = models.ProgresoGrafico
    form = forms.ProgresoGraficoForm
    extra = 0
# end class


class AdquisiscionMaterialInline(ExTabular):
    model = models.AdquisiscionMaterial
    extra = 0
# end class


class ActividadInline(ExTabular):
    model = models.Actividad
    readonly_fields = ['fecha_estimada', 'desface']  # 'fecha_completado',

    extra = 0

    def get_formset(self, request, obj=None, fields=None):
        self.form = forms.ActividadForm
        if obj and obj.personal.empleado:
            user = CuserMiddleware.get_user()
            empleado = EmpleadoU.objects.filter(
                _empleado=obj.personal.empleado).first()
            if user.pk == empleado.pk:
                print user, empleado
                self.form = forms.ActividadUserForm
            # end if
        # end if
        return super(ActividadInline, self).get_formset(request=request, obj=obj, fields=fields)
    # end def

    def get_queryset(self, request):
        queryset = super(ActividadInline, self).get_queryset(request)
        return queryset.order_by('poscicion')
    # end def
# end class


class ActividadAdmin(admin.ModelAdmin):
    form = forms.ActividadForm
    readonly_fields = ['fecha_completado', 'desface']
# end class


class OrdenTrabajoAdmin(nested_admin.NestedModelAdmin):
    inlines = [AdquisiscionMaterialInline,
               ActividadInline, ProgresoGraficoInline]
    readonly_fields = ['fecha_creacion']
    form = forms.OrdenTrabajoForm
# end class


class OrdenTrabajoInline(ExTab):
    model = models.OrdenTrabajo
    # form = forms.OrdenTrabajoForm
    # readonly_fields = ['fecha_final_estimada', 'fecha_final_real', ]
    inlines = [ActividadInline,
               AdquisiscionMaterialInline, ProgresoGraficoInline]
    extra = 0
# end class


class ProyectoAdmin(nested_admin.NestedModelAdmin):
    inlines = [OrdenTrabajoInline, GanttInline]
    emplate = 'admin/inlines/stackedTab.html'
# end class

exileui.register(models.Personal)
exileui.register(models.Grupo)
exileui.register(models.TipoAdquisiscion)
exileui.register(models.Material)
exileui.register(models.OrdenTrabajo, OrdenTrabajoAdmin)
exileui.register(models.Actividad, ActividadAdmin)
exileui.register(models.Proyecto, ProyectoAdmin)
