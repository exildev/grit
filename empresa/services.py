from models import Empresa, Departamento, Requisito, Cargo, Empleado, Jefes
from usr import models as usr
from forms import EmpresaForm, DepartamentoForm, RequisitoForm, CargoForm, EmpleadoForm, JefesForm
from django.db import connection
from django.db.models import Count
import json

class EmpresaService():

	def tabla_empresa(self, request):
		return Empresa.objects
	#end def

	def tabla_cargo(self, request):
		departamento = request.GET.get('departamento', False)
		return Cargo.objects.filter(departamento = departamento)
	#end def

	def panel_empresa(self, request):
		empresas = Empresa.objects.all()
		return empresas
	#end def

	def mostrar_empresa(self, request, pk):
		empresa = Empresa.objects.filter(pk = pk).first()
		if empresa:
			return empresa
		#end if
		return False
	#end def
	
	def mostrar_mi_empresa(self, request):
		empresa = usr.Empresa.objects.filter(usuario = request.user).first()
		if empresa:
			return empresa.empresa
		#end if
		return False
	#end def

	def form_empresa(self, request, empresa = None):
		if request.POST:
			return EmpresaForm(request.POST, request.FILES, instance = empresa)
		else:
			return EmpresaForm(instance = empresa)
		#end if
	#end def

	def crear_empresa(self, request):
		form = EmpresaForm(request.POST, request.FILES)
		if form.is_valid():
			empresa = form.save()
			return empresa, True
		#end if
		return form, False
	#end def

	def editar_empresa(self, request, pk):
		empresa = Empresa.objects.filter(pk = pk).first()
		if empresa:
			form = self.form_empresa(request, empresa)
			if form.is_valid():
				empresa = form.save()
				return empresa, True
			#end if
			return form, False
		#end if
		return None, False
	#end def


	def panel_departamento(self, request, empresa):
		cursor = connection.cursor()
		try:
			cursor.callproc('mapa_procesos')
			result_set = cursor.fetchall()
			return json.loads(result_set[0][0])
			#end if
		finally:
			cursor.close()
		#end try
		return False
	#end def

	def mostrar_departamento(self, request, pk):
		departamento = Departamento.objects.filter(pk = pk).first()
		if departamento:
			return departamento
		#end if
		return False
	#end def

	def form_editar_departamento(self, request, departamento):
		return DepartamentoForm(instance = departamento)
	#end def

	def form_departamento(self, request, departamento = None):
		if request.POST:
			return DepartamentoForm(request.POST, request.FILES, instance = departamento)
		else:
			return DepartamentoForm(instance = departamento)
		#end if
	#end def

	def crear_departamento(self, request):
		form = DepartamentoForm(request.POST, request.FILES)
		if form.is_valid():
			departamento = form.save()
			return departamento, True
		#end if
		return form, False
	#end def

	def editar_departamento(self, request, pk):
		departamento = Departamento.objects.filter(pk = pk).first()
		if departamento:
			form = DepartamentoForm(request.POST, request.FILES, instance = departamento)
			if form.is_valid():
				form.save()
				return departamento, True
			#end if
			return form, False
		#end if
		return None, False
	#end def

	def panel_cargo(self, request, empresa = None, departamento = None):
		cargos = Cargo.objects.all()
		if empresa:
			cargos = cargos.filter(departamento__empresa__pk = empresa)
		#end if
		if departamento:
			cargos = cargos.filter(departamento__pk = departamento)
		#end if
		cargos = cargos.annotate(empleados=Count('empleado'))
		return cargos
	#end def

	def mostrar_cargo(self, request, pk):
		cargo = Cargo.objects.filter(pk = pk).first()
		if cargo:
			return cargo
		#end if
		return False
	#end def

	def form_editar_cargo(self, request, cargo):
		return CargoForm(instance = cargo)
	#end def

	def form_cargo(self, request, cargo = None):
		if request.POST:
			return CargoForm(request.POST, request.FILES, instance = cargo)
		else:
			return CargoForm(instance = cargo)
		#end if
	#end def

	def crear_cargo(self, request):
		form = CargoForm(request.POST, request.FILES)
		if form.is_valid():
			cargo = form.save()
			return cargo, True
		#end if
		return form, False
	#end def

	def editar_cargo(self, request, pk):
		cargo = Cargo.objects.filter(pk = pk).first()
		if cargo:
			form = CargoForm(request.POST, request.FILES, instance = cargo)
			if form.is_valid():
				form.save()
				return cargo, True
			#end if
			return form, False
		#end if
		return None, None
	#end def

	def mostrar_requisito(self, request, cargo):
		requisito = Requisito.objects.filter(cargo = cargo).first()
		if requisito:
			return requisito
		#end if
		return False
	#end def

	def form_requisito(self, request, cargo):
		requisito = self.mostrar_requisito(request, cargo)
		if requisito:
			if request.POST:
				return RequisitoForm(request.POST, request.FILES, instance = requisito)
			else:
				return RequisitoForm(instance = requisito)
			#end if
		#end if
		return RequisitoForm()
	#end def

	def crear_requisito(self, request, cargo):
		form = RequisitoForm(request.POST)
		cargos = Cargo.objects.filter(pk = cargo).count()
		if cargos and form.is_valid():
			requisito = form.save()
			Cargo.objects.filter(pk = cargo).update(requisito = requisito)
			return requisito, True
		#end if
		return form, False
	#end def

	def editar_requisito(self, request, pk):
		requisito = Requisito.objects.filter(cargo__pk = pk).first()
		if requisito:
			form = RequisitoForm(request.POST, request.FILES, instance = requisito)
			if form.is_valid():
				form.save()
				return requisito, True
			#end if
			return form, False
		#end if
		return None, False
	#end def

	def panel_empleado(self, request, cargo ):
		empleados = Empleado.objects.filter(cargo = cargo)
		return empleados
	#end def

	def form_empleado(self, request, empleado = None):
		if request.POST:
			return EmpleadoForm(request.POST, request.FILES, instance = empleado)
		else:
			return EmpleadoForm(instance = empleado)
		#end if
	#end def

	def mostrar_empleado(self, request, pk):
		empleados = Empleado.objects.filter(pk = pk)[:1]
		if len(empleados):
			return empleados[0]
		#end if
		return False
	#end def

	def crear_empleado(self, request):
		form = EmpleadoForm(request.POST, request.FILES)
		if form.is_valid():
			empleado = form.save(commit=False)
			notificable = Notificable.objects.get(pk = empleado.cargo.pk)
			empleado.notificable = notificable
			empleado.save()
			return empleado, True
		#end if
		return form, False
	#end def

	def editar_empleado(self, request, pk):
		empleado = Empleado.objects.filter(pk = pk).first()
		if empleado:
			form = EmpleadoForm(request.POST, request.FILES, instance = empleado)
			if form.is_valid():
				form.save()
				return empleado, True
			#end if
			return form, False
		#end if
		return None, False
	#end def

	def mostrar_jefes(self, request, departamento):
		jefes = Jefes.objects.filter(departamento__pk = departamento).first()
		if jefes:
			return jefes
		#end if
		return False
	#end def

	def form_jefes(self, request, departamento):
		jefes = self.mostrar_jefes(request, departamento)
		if jefes:
			if request.POST:
				return JefesForm(request.POST, request.FILES, instance = jefes)
			else:
				return JefesForm(instance = jefes)
			#end if
		#end if
		return JefesForm()
	#end def

	def crear_jefes(self, request):
		form = JefesForm(request.POST, request.FILES)
		if form.is_valid():
			jefes = form.save()
			return jefes, True
		#end if
		return form, False
	#endd def

	def editar_jefes(self, request, pk):
		jefes = Jefes.objects.filter(departamento__pk = pk).first()
		if jefes:
			form = JefesForm(request.POST, request.FILES, instance = jefes)
			if form.is_valid():
				form.save()
				return jefes, True
			#end if
			return form, False
		#end if
		return None, False
	#end def
#end class