# -*- encoding: utf8 -*-
from exileui.admin import exileui
from exileui.admin import exileui, ExStacked, ExTabular, ExTab, DateRangeEX, DateRangeEX, ExGraph
from django.contrib.admin.views.main import ChangeList
from django.db.models import Sum, Avg
from usr.models import Empleado as EmpleadoU
from cuser.middleware import CuserMiddleware
from django.contrib import admin
import nested_admin
import models
import forms

class TotalAveragesChangeList(ChangeList):
    #provide the list of fields that we need to calculate averages and totals
    fields_to_total = ['amount', 'total_sum', 'paid_by_cash',
                       'paid_by_transfer',]
 
 
 
    def get_total_values(self, queryset):
        """
        Get the totals
        """
        #basically the total parameter is an empty instance of the given model
        total = models.Actividad(nombre='total dias', dias_estimados=queryset.aggregate(dias_estimados=Sum('dias_estimados'))['dias_estimados'])
        return total

 
    def get_results(self, request):
        """
        The model admin gets queryset results from this method
        and then displays it in the template
        """
        super(TotalAveragesChangeList, self).get_results(request)
        #first get the totals from the current changelist
        total = self.get_total_values(self.queryset)
        #then get the averages
        #small hack. in order to get the objects loaded we need to call for 
        #queryset results once so simple len function does it
        len(self.result_list)
        #and finally we add our custom rows to the resulting changelist
        self.result_list._result_cache.append(total)
# end class


class GanttInline(nested_admin.NestedStackedInline):
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
    list_display = ['nombre', 'dias_estimados']

    def get_changelist(self, request, **kwargs):
        return TotalAveragesChangeList
    # end def
# end class


class OrdenTrabajoAdmin(nested_admin.NestedModelAdmin):
    inlines = [AdquisiscionMaterialInline,
               ActividadInline, ProgresoGraficoInline]
    readonly_fields = ['fecha_creacion']
    form = forms.OrdenTrabajoForm
# end class


class OrdenTrabajoInline(ExGraph):
    model = models.OrdenTrabajo
    # form = forms.OrdenTrabajoForm
    # readonly_fields = ['fecha_final_estimada', 'fecha_final_real', ]
    inlines = [ActividadInline,
               AdquisiscionMaterialInline, ProgresoGraficoInline]
    extra = 0

    def __init__(self, *args, **kwargs):
        super(OrdenTrabajoInline, self).__init__(*args, **kwargs)
    # end def
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
