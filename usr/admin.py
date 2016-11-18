# -*- encoding: utf8 -*-
from exileui.admin import exileui
from django.contrib import admin
import forms
from models import Empresa, Auditor, Administrador, Empleado

class EmpleadoAdmin(admin.ModelAdmin):
	model = Empleado
	form = forms.EmpleadoForm
#end class

class EmpresaAdmin(admin.ModelAdmin):
	model = Empresa
	form = forms.EmpresaForm
#end class

#exileui.register(Empresa, EmpresaAdmin)
#exileui.register(Auditor)
#exileui.register(Administrador)
#exileui.register(Empleado, EmpleadoAdmin)