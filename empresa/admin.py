# -*- coding: utf-8 -*-
from exileui.admin import exileui
from django.contrib import admin
import forms
from django.db.models import Q
import models as empresa
from usr import  models as usr
from usr import forms as usr_form
from cuser.middleware import CuserMiddleware
from grit import forms as grit

class EmpresaUsrInline(admin.StackedInline):
    form = grit.UserForm
    model = usr.Empresa
#end class

class EmpresaAdmin(admin.ModelAdmin):
    model = empresa.Empresa
    form = forms.EmpresaForm
    inlines = [EmpresaUsrInline]
#end class

class CargoStacked(admin.StackedInline):
    model = empresa.Cargo
    form = forms.CargoForm
#end class

class DepartamentoAdmin(admin.ModelAdmin):
    model = empresa.Departamento
    list_display  = ('nombre', 'empresa')
    search_fields = ('nombre', )
    list_filter   = ('nombre', )


    def get_form(self, request, obj=None, **kwargs):
        if request.user.is_superuser:
            self.form =  forms.DepartamentoAdminForm
        else:
            self.form = forms.DepartamentoAdminForm
        #end if
        return super(DepartamentoAdmin, self).get_form(request, obj, **kwargs)
    #end def

    def get_queryset(self, request):
        queryset = super(DepartamentoAdmin, self).get_queryset(request)
        user = CuserMiddleware.get_user()
        if not request.user.is_superuser:
            queryset = queryset.filter(empresa__empresa = user)
        # end if
        return queryset
    #end def
#end class

class RequisitoAdmin(admin.ModelAdmin):
    model = empresa.Requisito
    form = forms.RequisitoForm
#end class

class RequisitoStacked(admin.StackedInline):
    model = empresa.Requisito
    form = forms.RequisitoForm
#end class

class EmpleadoStacked(admin.StackedInline):
    model = empresa.Empleado
    form = forms.EmpleadoForm
#end class


class CargoAdmin(admin.ModelAdmin):
    model = empresa.Cargo
    form = forms.CargoForm
    list_display  = ('nombre', 'departamento', 'salario')
    search_fields = ('nombre', 'departamento__nombre')
    list_filter   = ('nombre', 'departamento', 'salario')
    inlines       = (RequisitoStacked, )
    #raw_id_fields = ('departamento', )
    
    def get_queryset(self, request):
        queryset = super(CargoAdmin, self).get_queryset(request)
        user = CuserMiddleware.get_user()
        if not request.user.is_superuser:
            queryset = queryset.filter(departamento__empresa__empresa = user)
        # end if
        return queryset
    #end def
#end class

class EmpleadoUsrStacked(admin.StackedInline):
    model = usr.Empleado
    form = usr_form.EmpleadoForm
#end def

class EmpleadoAdmin(admin.ModelAdmin):
    model = empresa.Empleado
    inlines = [EmpleadoUsrStacked]
    list_filter = ('cargo',)
    search_fields = ('codigo', 'nombre', 'apellido')
    list_display  = ('codigo', 'nombre', 'apellido', 'cargo', 'empresa', 'salario')

    def get_readonly_fields(self, request, obj=None):
        if obj != None and obj.cargo != None:
            return ['cargo', 'empresa']
        #end if
        return []
    #end def
    
    def get_form(self, request, obj=None, **kwargs):
        if obj != None and obj.cargo != None:
            self.form =  forms.EmpleadoEditForm
        else:
            self.form = forms.EmpleadoForm
        #end if
        return super(EmpleadoAdmin, self).get_form(request, obj, **kwargs)
    #end def

    def get_queryset(self, request):
        qs = super(EmpleadoAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        #end if

        user = CuserMiddleware.get_user()
        empres = empresa.Empresa.objects.filter(empresa = user).first()
        if empres:
            return qs.filter(empresa = empres)
        #end if
        return qs.filter(empleado = user)
    #end def
#end class

class JefesAdmin(admin.ModelAdmin):
    model = empresa.Jefes
    form = forms.JefesForm
#end class

class ContratoAdmin(admin.ModelAdmin):
    search_fields = ['empleado__nombre', 'empleado__apellido', 'fecha_inicio']
    list_filter = ('cargo__nombre', 'fecha_inicio')
    list_display = ['empleado', 'cargo', 'fecha_inicio']
    model = empresa.Contrato
    form = forms.ContratoForm
#end class

class LiquidacionNominaAdmin(admin.ModelAdmin):
    search_fields = ['empleado__nombre', 'empleado__apellido', 'fecha', 'periodo']
    list_filter  = ('empleado__cargo__nombre', 'fecha')
    list_display = ['empleado', 'periodo', 'fecha_corte', 'totl']
    model = empresa.LiquidacionNomina
    def get_form(self, request, obj=None, **kwargs):
        if obj != None:
            self.readonly_fields = ('dias', 'hord','cesa', 'intc', 'prim', 'hexd', 'hexn', 'hxdd', 'hxnd', 'totl')
            self.form =  forms.LiquidacionNominaEditForm
        else:
            self.readonly_fields = ()
            self.form = forms.LiquidacionNominaCreateForm
        #end if
        return super(LiquidacionNominaAdmin, self).get_form(request, obj, **kwargs)
    #end def
#end class

exileui.register(empresa.Asistencia)
exileui.register(empresa.HorasExtra)
exileui.register(empresa.Configuracion)
exileui.register(empresa.LiquidacionNomina, LiquidacionNominaAdmin)
exileui.register(empresa.Calculos)
exileui.register(empresa.Empresa, EmpresaAdmin)
exileui.register(empresa.Departamento, DepartamentoAdmin)
#exileui.register(empresa.Requisito, RequisitoAdmin)
exileui.register(empresa.Cargo, CargoAdmin)
exileui.register(empresa.Empleado, EmpleadoAdmin)
exileui.register(empresa.Contrato, ContratoAdmin)
#exileui.register(empresa.Jefes, JefesAdmin)