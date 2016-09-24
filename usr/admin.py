# -*- encoding: utf8 -*-
from exile_ui.admin import admin_site
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

#admin_site.register(Empresa, EmpresaAdmin)
#admin_site.register(Auditor)
#admin_site.register(Administrador)
#admin_site.register(Empleado, EmpleadoAdmin)