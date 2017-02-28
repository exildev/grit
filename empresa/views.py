from services import EmpresaService
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from usr.decorators import administrador, empresa
from huella.decorators import datatable
from django.db.models import Count
import json as simplejson

#@datatable(['codigo', 'razons', 'ident', 'telefono', 'ciudad', 'activo', 'logo', 'email', 'direccion'])
def test_empresa(request):
	return render(request, 'empresa/tabla.html')
#end def

@datatable(['codigo', 'razons', 'ident', 'telefono', 'ciudad', 'activo', 'logo', 'email', 'direccion'])
def json_empresa(request):
	empresas = EmpresaService().tabla_empresa(request)
	return empresas
#end def

@datatable(['nombre'], ['nombre', 'requisito', 'empleados', 'agregar', 'editar'], annotate={'empleados':Count('empleado')}, extras={'editar':'notificable_ptr_id', 'agregar':'notificable_ptr_id', 'requisito': "'[' || coalesce(requisito_id, 0) || ', ' || notificable_ptr_id || ']'"})
def json_cargo(request):
	cargos = EmpresaService().tabla_cargo(request)
	return cargos
#end def

def panel_empresa(request):
	empresas = EmpresaService().panel_empresa(request)
	return render(request, 'empresa/panel_empresa.html', {'empresas': empresas})
#end def
 
def form_crear_empresa(request, form = None, hecho = None):
	hecho = request.GET.get('hecho', hecho)
	services = EmpresaService()
	if not form:
		form = services.form_empresa(request)
	#ende if
	return render(request, 'empresa/form_empresa.html', {'form': form, 'hecho': hecho})
#end def

def form_editar_empresa(request, empresa, form = None, hecho = None):
	hecho = request.GET.get('hecho', hecho)
	services = EmpresaService()
	empresa = services.mostrar_empresa(request, empresa)
	if empresa:
		if not form:
			form = services.form_empresa(request, empresa)
		#ende if
		return render(request, 'empresa/form_empresa.html', {'form': form, 'hecho': hecho})
	#end if
	raise Http404
#end def

def crear_empresa(request):
	modo = request.POST.get('modo', False)
	services = EmpresaService() 
	empresa, hecho = services.crear_empresa(request)
	if hecho:
		if   modo == 'h':
			return redirect(reverse(panel_empresa))
		elif modo == 's':
			return redirect(reverse(form_empresa)+'?hecho='+hecho)
		elif modo == 'm':
			return redirect(reverse(mostrar_empresa, kwargs = {'empresa':empresa.pk}))
		#end if
	#end if
	return form_crear_empresa(request, form = empresa, hecho='false')
#end def

def editar_empresa(request, empresa):
	modo = request.POST.get('modo', False)
	services = EmpresaService()
	empresa, hecho = services.editar_empresa(request, empresa)
	if hecho:
		if   modo == 'h':
			return redirect(reverse(panel_empresa))
		elif modo == 's':
			return redirect(reverse(form_editar_empresa, kwargs={'empresa': empresa.pk})+'?hecho=true')
		elif modo == 'm':
			return redirect(reverse(mostrar_empresa, kwargs={'empresa':empresa.pk}))
		#end if
	#end if
	return form_editar_empresa(request, empresa.instance.pk, form = empresa, hecho='false')
#end def

def mostrar_empresa(request, empresa):
	empresa = EmpresaService().mostrar_empresa(request, empresa)
	if empresa:
		return render(request, 'empresa/mostrar_empresa.html', {'empresa': empresa})
	else:
		raise Http404
	#end if
#end def

def panel_departamento(request):
	service = EmpresaService()
	empresa = service.mostrar_mi_empresa(request)
	if empresa:
		departamentos = service.panel_departamento(request, empresa)
		return render(request, 'empresa/index.html', {'departamentos': departamentos, 'empresa': empresa})
	#end if
	raise Http404
#end def

def form_crear_departamento(request, empresa, form = None, hecho = None):
	hecho = request.GET.get('hecho', hecho)
	services = EmpresaService()
	empresa  = services.mostrar_empresa(request, empresa)
	if empresa:
		if not form:
			form = services.form_departamento(request)
		#ende if
		return render(request, 'empresa/form_departamento.html', {'form': form, 'hecho': hecho, 'empresa': empresa})
	#end if
	raise Http404
#end def

def form_editar_departamento(request, departamento, form = None, form_jefes = None, hecho = None):
	hecho = request.GET.get('hecho', hecho)
	services = EmpresaService()
	departamento = services.mostrar_departamento(request, departamento)
	if departamento:
		if not form:
			form = services.form_editar_departamento(request, departamento)
		#ende if
		if not form_jefes:
			form_jefes = services.form_jefes(request, departamento.pk)
		#end if
		return render(request, 'empresa/form_departamento.html', {'form': form, 'form_jefes': form_jefes,'hecho': hecho})
	#end if
	raise Http404
#end def

def crear_departamento(request):
	modo = request.POST.get('modo', False)
	services = EmpresaService() 
	departamento, hecho = services.crear_departamento(request)
	if hecho:
		if   modo == 'h':
			return redirect(reverse(panel_departamento, kwargs = {'empresa': departamento.empresa.id}))
		elif modo == 's':
			return redirect(reverse(form_departamento, kwargs = {'empresa': departamento.empresa.id})+'?hecho='+hecho)
		elif modo == 'm':
			return redirect(reverse(mostrar_departamento, kwargs = {'departamento':departamento.pk}))
		#end if
	#end if
	return form_crear_departamento(request, departamento['empresa'], form = departamento, hecho = 'false')
#end def

def editar_departamento(request, departamento):
	modo = request.POST.get('modo', False)
	services = EmpresaService()
	departamento, hecho = services.editar_departamento(request, departamento)
	if hecho:
		if   modo == 'h':
			return redirect(reverse(panel_departamento, kwargs = {'empresa': departamento.empresa.id}))
		elif modo == 's':
			return redirect(reverse(form_editar_departamento, kwargs={'departamento': departamento.pk})+'?hecho=true')
		elif modo == 'm':
			return redirect(reverse(mostrar_departamento, kwargs={'departamento':departamento.pk}))
		#end if
	#end if
	return form_editar_departamento(request, departamento.instance.pk, form = departamento, hecho = 'false')
#end def

def mostrar_departamento(request, departamento):
	services = EmpresaService()
	departamento = services.mostrar_departamento(request, departamento)
	if departamento:
		jefes = services.mostrar_jefes(request, departamento.pk)
		return render(request, 'empresa/mostrar_departamento.html', {'departamento': departamento, 'jefes': jefes})
	else:
		raise Http404
	#end if
#end def

def panel_cargo(request, departamento):
	services = EmpresaService()
	departamento = services.mostrar_departamento(request, departamento)
	if departamento:
		cargos = services.panel_cargo(request, departamento=departamento.pk)
		return render(request, 'empresa/panel_cargo.html', {'cargos': cargos, 'departamento': departamento})
	#end if
	raise Http404
#end def

def form_crear_cargo(request, departamento, form = None, hecho = None):
	hecho = request.GET.get('hecho', hecho)
	services = EmpresaService()
	departamento  = services.mostrar_departamento(request, departamento)
	if departamento:
		if not form:
			form = services.form_cargo(request)
		#ende if
		return render(request, 'empresa/form_cargo.html', {'form': form, 'hecho': hecho, 'departamento': departamento})
	#end if
	raise Http404
#end def

def form_editar_cargo(request, cargo, form = None, form_requisito = None, hecho = None):
	hecho = request.GET.get('hecho', hecho)
	services = EmpresaService()
	cargo = services.mostrar_cargo(request, cargo)
	if cargo:
		if not form:
			form = services.form_editar_cargo(request, cargo)
		#ende if
		if not form_requisito:
			form_requisito = services.form_requisito(request, cargo)
		#ende if
		return render(request, 'empresa/form_cargo.html', {'form': form, 'form_requisito': form_requisito, 'hecho': hecho})
	#end if
	raise Http404
#end def


def crear_cargo(request):
	modo = request.POST.get('modo', False)
	services = EmpresaService()
	cargo, hecho = services.crear_cargo(request)
	if hecho:
		return HttpResponse()
	#end if
	return HttpResponse(simplejson.dumps(cargo.errors), status=400)
#end def

def editar_cargo(request, cargo):
	modo = request.POST.get('modo', False)
	services = EmpresaService()
	cargo, hecho = services.editar_cargo(request, cargo)
	if hecho:
		return HttpResponse()
	#end if
	return HttpResponse(simplejson.dumps(cargo.errors), status=400)
#end def

def mostrar_cargo(request, cargo):
	services = EmpresaService()
	cargo = services.mostrar_cargo(request, cargo)	
	if cargo:
		requisito = services.mostrar_requisito(request, cargo.pk)
		return render(request, 'empresa/mostrar_cargo.html', {'cargo': cargo, 'requisito': requisito})
	#end if
	raise Http404
#end def
def form_crear_requisito(request, cargo, form = None, hecho = None):
	hecho = request.GET.get('hecho', hecho)
	services = EmpresaService()
	cargo  = services.mostrar_cargo(request, cargo)
	if cargo:
		if not form:
			form = services.form_requisito(request, cargo)
		#ende if
		return render(request, 'empresa/form_requisito.html', {'form': form, 'hecho': hecho, 'cargo': cargo})
	#end if
	raise Http404
#end def

def form_editar_requisito(request, cargo, form = None, form_requisito = None, hecho = None):
	hecho = request.GET.get('hecho', hecho)
	services = EmpresaService()
	cargo  = services.mostrar_cargo(request, cargo)
	if cargo:
		if not form:
			form = services.form_requisito(request, cargo)
		#ende if
		return render(request, 'empresa/form_requisito.html', {'form': form, 'hecho': hecho, 'cargo': cargo})
	#end if
	raise Http404
#end def

def crear_requisito(request, cargo):
	modo = request.POST.get('modo', False)
	services = EmpresaService()
	requisito, hecho = services.crear_requisito(request, cargo)
	if hecho:
		return HttpResponse()
	#end if
	return HttpResponse(simplejson.dumps(requisito.errors), status="400")
#end def

def editar_requisito(request, cargo):
	modo = request.POST.get('modo', False)
	services = EmpresaService()
	requisito, hecho = services.editar_requisito(request, cargo)
	if hecho:
		return HttpResponse()
	#end if
	return HttpResponse(simplejson.dumps(requisito.errors), status="400")
#end def

def panel_empleado(request, cargo):
	services = EmpresaService()
	cargo = services.mostrar_cargo(request, cargo)
	if cargo:
		empleados = services.panel_empleado(request, cargo.pk)
		return render(request, 'empresa/panel_empleado.html', {'cargo':cargo,'empleados': empleados})
	#end if
	raise Http404
#end def

def form_crear_empleado(request, cargo, form = None, hecho = None):
	hecho = request.GET.get('hecho', hecho)
	services = EmpresaService()
	cargo  = services.mostrar_cargo(request, cargo)
	if cargo:
		if not form:
			form = services.form_empleado(request)
		#ende if
		return render(request, 'empresa/form_empleado.html', {'form': form, 'hecho': hecho, 'cargo': cargo})
	#end if
	raise Http404
#end def

def form_editar_empleado(request, empleado, form = None, hecho = None):
	hecho = request.GET.get('hecho', hecho)
	services = EmpresaService()
	empleado = services.mostrar_empleado(request, empleado)
	if empleado:
		if not form:
			form = services.form_empleado(request, empleado)
		#ende if
		return render(request, 'empresa/form_empleado.html', {'form': form, 'hecho': hecho})
	#end if
	raise Http404
#end def

def crear_empleado(request):
	modo = request.POST.get('modo', False)
	services = EmpresaService()
	empleado, hecho = services.crear_empleado(request)
	if hecho:
		if   modo == 'h':
			return redirect(reverse(panel_empleado, kwargs={'cargo':empleado.cargo.pk}))
		elif modo == 's':
			return redirect(reverse(form_crear_empleado, kwargs={'cargo': empleado.cargo.pk}) + '?hecho=true')
		elif modo == 'm':
			return redirect(reverse(mostrar_empleado, kwargs={'empleado':empleado.pk}))
		#end if
	#end if
	return form_crear_empleado(request, cargo=empleado['cargo'].value, form=empleado, hecho='false')
#end def

def editar_empleado(request, empleado):
	modo = request.POST.get('modo', False)
	services = EmpresaService()
	empleado, hecho = services.editar_empleado(request, empleado)
	if hecho:
		if   modo == 'h':
			return redirect(reverse(panel_empleado, kwargs={'cargo':empleado.cargo.pk}))
		elif modo == 's':
			return redirect(reverse(form_editar_empleado, kwargs={'empleado': empleado.pk}) + '?hecho=true')
		elif modo == 'm':
			return redirect(reverse(mostrar_empleado, kwargs={'empleado':empleado.pk}))
		#end if
	#end if
	return form_editar_empleado(request, empleado=empleado.instance.pk, form=empleado, hecho='false')
#end def

def mostrar_empleado(request, empleado):
	if empleado:
		empleado = EmpresaService().mostrar_empleado(request, empleado)
		empresa = empleado.cargo.departamento.empresa
		departamento = empleado.cargo.departamento
	#end if
	if empresa:
		departamentos = EmpresaService().panel_departamento(request, empresa.pk)
	#end if
	return render(request, 'empresa/mostrar_empleado.html', {'empresa': empresa, 'departamento': departamento, 'departamentos': departamentos, 'empleado': empleado})
#end def

def crear_jefes(request):
	modo = request.POST.get('modo', False)
	services = EmpresaService()
	jefes, hecho = services.crear_jefes(request)
	if hecho:
		return redirect(reverse(mostrar_departamento, kwargs={'departamento':jefes.departamento.pk}))
	#end if
	return form_editar_departamento(request, departamento=jefes['departamento'].value, form_jefes = jefes, hecho='false')
#end def

def editar_jefes(request, departamento):
	modo = request.POST.get('modo', False)
	services = EmpresaService()
	jefes, hecho = services.editar_jefes(request, departamento)
	if hecho:
		return redirect(reverse(mostrar_departamento, kwargs={'departamento':departamento}))
	#end if
	return form_editar_departamento(request, departamento=departamento, form_jefes = jefes, hecho='false')
#end def

