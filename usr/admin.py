<<<<<<< HEAD
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
=======
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
>>>>>>> d4a43d94c0aa6b0b9855c268cd630ce06cd3af9c
