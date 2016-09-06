from services import RiesgoService
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

def panel_criticidad(request):
	services = RiesgoService()
	criticidads = services.panel_criticidad(request)
	return render(request, 'riesgo/panel_criticidad.html', {'criticidads':criticidads})
#end def

def mostrar_criticidad(request, criticidad):
	services = RiesgoService()
	criticidad = services.mostrar_criticidad(request, criticidad)
	if criticidad:
		return render(request, 'riesgo/mostrar_criticidad.html',{'criticidad':criticidad})
	#end if
	raise Http404
#end def

def form_crear_criticidad(request, form=None, hecho=None):
	hecho = request.POST.get('hecho', hecho)
	services = RiesgoService()
	if not form:
		form = services.form_criticidad(request)
	#end if
	return render(request, 'riesgo/form_criticidad.html', {'form': form, 'hecho': hecho})
#end def

def form_editar_criticidad(request, criticidad, form=None, hecho=None):
	hecho = request.POST.get('hecho', hecho)
	services = RiesgoService()
	criticidad = services.mostrar_criticidad(request, criticidad)
	if criticidad:
		if not form:
			form = services.form_criticidad(request, criticidad)
		#end if
		return render(request, 'riesgo/form_criticidad.html', {'criticidad': criticidad, 'form': form})
	#end if
	raise Http404
#end def

def crear_criticidad(request):
	modo = request.POST.get('modo', False)
	services = RiesgoService()
	criticidad, hecho = services.crear_criticidad(request)
	if hecho:
		if   modo == 'h':
			return redirect(reverse(panel_criticidad))
		elif modo == 's':
			return redirect(reverse(form_crear_criticidad, kwargs={})+'?hecho=true')
		elif modo == 'm':
			return redirect(reverse(mostrar_criticidad, kwargs={'criticidad': criticidad.pk}))
		#end if
	#end if
	return form_crear_criticidad(request, form=criticidad, hecho='false')
#end def

def editar_criticidad(request, criticidad):
	modo = request.POST.get('modo', False)
	services = RiesgoService()
	criticidad, hecho = services.editar_criticidad(request, criticidad)
	if hecho:
		if   modo == 'h':
			return redirect(reverse(panel_criticidad))
		elif modo == 's':
			return redirect(reverse(form_editar_criticidad, kwargs={'criticidad':criticidad.pk})+'?hecho=true')
		elif modo == 'm':
			return redirect(reverse(mostrar_criticidad, kwargs={'criticidad': criticidad.pk}))
		#end if
	#end if
	return form_editar_criticidad(request, criticidad.instance.pk, form=criticidad, hecho='false')
#end def

def panel_elementoproteger(request):
	services = RiesgoService()
	elementoprotegers = services.panel_elementoproteger(request)
	return render(request, 'riesgo/panel_elementoproteger.html', {'elementoprotegers':elementoprotegers})
#end def

def mostrar_elementoproteger(request, elementoproteger):
	services = RiesgoService()
	elementoproteger = services.mostrar_elementoproteger(request, elementoproteger)
	if elementoproteger:
		return render(request, 'riesgo/mostrar_elementoproteger.html',{'elementoproteger':elementoproteger})
	#end if
	raise Http404
#end def

def form_crear_elementoproteger(request, form=None, hecho=None):
	hecho = request.POST.get('hecho', hecho)
	services = RiesgoService()
	if not form:
		form = services.form_elementoproteger(request)
	#end if
	return render(request, 'riesgo/form_elementoproteger.html', {'form': form, 'hecho': hecho})
#end def

def form_editar_elementoproteger(request, elementoproteger, form=None, hecho=None):
	hecho = request.POST.get('hecho', hecho)
	services = RiesgoService()
	elementoproteger = services.mostrar_elementoproteger(request, elementoproteger)
	if elementoproteger:
		if not form:
			form = services.form_elementoproteger(request, elementoproteger)
		#end if
		return render(request, 'riesgo/form_elementoproteger.html', {'elementoproteger': elementoproteger, 'form': form})
	#end if
	raise Http404
#end def

def crear_elementoproteger(request):
	modo = request.POST.get('modo', False)
	services = RiesgoService()
	elementoproteger, hecho = services.crear_elementoproteger(request)
	if hecho:
		if   modo == 'h':
			return redirect(reverse(panel_elementoproteger))
		elif modo == 's':
			return redirect(reverse(form_crear_elementoproteger)+'?hecho=true')
		elif modo == 'm':
			return redirect(reverse(mostrar_elementoproteger, kwargs={'elementoproteger': elementoproteger.pk}))
		#end if
	#end if
	return form_crear_elementoproteger(request, form=elementoproteger, hecho='false')
#end def

def editar_elementoproteger(request, elementoproteger):
	modo = request.POST.get('modo', False)
	services = RiesgoService()
	elementoproteger, hecho = services.editar_elementoproteger(request, elementoproteger)
	if hecho:
		if   modo == 'h':
			return redirect(reverse(panel_elementoproteger))
		elif modo == 's':
			return redirect(reverse(form_editar_elementoproteger, kwargs={'elementoproteger':elementoproteger.pk})+'?hecho=true')
		elif modo == 'm':
			return redirect(reverse(mostrar_elementoproteger, kwargs={'elementoproteger': elementoproteger.pk}))
		#end if
	#end if
	return form_editar_elementoproteger(request, elementoproteger.instance.pk, form=elementoproteger, hecho='false')
#end def

def panel_cargoriesgo(request):
	services = RiesgoService()
	cargos = services.panel_cargo(request)
	cargoriesgos = services.panel_cargoriesgo(request)
	return render(request, 'riesgo/panel_cargoriesgo.html', {'cargos': cargos, 'cargoriesgos':cargoriesgos})
#end def

def mostrar_cargoriesgo(request, cargo):
	services = RiesgoService()
	cargoriesgo = services.mostrar_cargoriesgo_cargo(request, cargo)
	if cargoriesgo:
		return render(request, 'riesgo/mostrar_cargoriesgo.html',{'cargoriesgo':cargoriesgo})
	#end if
	return redirect(reverse(form_crear_cargoriesgo, kwargs={'cargo':cargo}))
#end def

def form_crear_cargoriesgo(request, cargo, form=None, hecho=None):
	hecho = request.POST.get('hecho', hecho)
	services = RiesgoService()
	cargo = services.mostrar_cargo(request, cargo)
	if cargo:
		if not form:
			form = services.form_cargoriesgo(request)
		#end if
		return render(request, 'riesgo/form_cargoriesgo.html', {'form': form, 'cargo':cargo, 'hecho': hecho})
	#end if
	raise Http404
#end def

def form_editar_cargoriesgo(request, cargoriesgo, form=None, hecho=None):
	hecho = request.POST.get('hecho', hecho)
	services = RiesgoService()
	cargoriesgo = services.mostrar_cargoriesgo(request, cargoriesgo)
	if cargoriesgo:
		if not form:
			form = services.form_cargoriesgo(request, cargoriesgo)
		#end if
		return render(request, 'riesgo/form_cargoriesgo.html', {'cargoriesgo': cargoriesgo, 'form': form})
	#end if
	raise Http404
#end def

def crear_cargoriesgo(request):
	modo = request.POST.get('modo', False)
	services = RiesgoService()
	cargoriesgo, hecho = services.crear_cargoriesgo(request)
	if hecho:
		if   modo == 'h':
			return redirect(reverse(panel_cargoriesgo, kwargs={}))
		elif modo == 's':
			return redirect(reverse(form_crear_cargoriesgo, kwargs={})+'?hecho=true')
		elif modo == 'm':
			return redirect(reverse(mostrar_cargoriesgo, kwargs={'cargoriesgo': cargoriesgo.pk}))
		#end if
	#end if
	return form_crear_cargoriesgo(request, cargoriesgo['cargo'].value(), form=cargoriesgo, hecho='false')
#end def

def editar_cargoriesgo(request, cargoriesgo):
	modo = request.POST.get('modo', False)
	services = RiesgoService()
	cargoriesgo, hecho = services.editar_cargoriesgo(request, cargoriesgo)
	if hecho:
		if   modo == 'h':
			return redirect(reverse(panel_cargoriesgo, kwargs={}))
		elif modo == 's':
			return redirect(reverse(form_editar_cargoriesgo, kwargs={'cargoriesgo':cargoriesgo.pk})+'?hecho=true')
		elif modo == 'm':
			return redirect(reverse(mostrar_cargoriesgo, kwargs={'cargoriesgo': cargoriesgo.pk}))
		#end if
	#end if
	return form_editar_cargoriesgo(request, cargoriesgo.instance.pk, form=cargoriesgo, hecho='false')
#end def

def panel_riesgo(request):
	services = RiesgoService()
	riesgos = services.panel_riesgo(request)
	return render(request, 'riesgo/panel_riesgo.html', {'riesgos':riesgos})
#end def

def mostrar_riesgo(request, riesgo):
	services = RiesgoService()
	riesgo = services.mostrar_riesgo(request, riesgo)
	if riesgo:
		return render(request, 'riesgo/mostrar_riesgo.html',{'riesgo':riesgo})
	#end if
	raise Http404
#end def

def form_crear_riesgo(request, form=None, hecho=None):
	hecho = request.POST.get('hecho', hecho)
	services = RiesgoService()
	if not form:
		form = services.form_riesgo(request)
	#end if
	return render(request, 'riesgo/form_riesgo.html', {'form': form, 'hecho': hecho})
#end def

def form_editar_riesgo(request, riesgo, form=None, hecho=None):
	hecho = request.POST.get('hecho', hecho)
	services = RiesgoService()
	riesgo = services.mostrar_riesgo(request, riesgo)
	if riesgo:
		if not form:
			form = services.form_riesgo(request, riesgo)
		#end if
		return render(request, 'riesgo/form_riesgo.html', {'riesgo': riesgo, 'form': form})
	#end if
	raise Http404
#end def

def crear_riesgo(request):
	modo = request.POST.get('modo', False)
	services = RiesgoService()
	riesgo, hecho = services.crear_riesgo(request)
	if hecho:
		if   modo == 'h':
			return redirect(reverse(panel_riesgo, kwargs={}))
		elif modo == 's':
			return redirect(reverse(form_crear_riesgo, kwargs={})+'?hecho=true')
		elif modo == 'm':
			return redirect(reverse(mostrar_riesgo, kwargs={'riesgo': riesgo.pk}))
		#end if
	#end if
	return form_crear_riesgo(request, form=riesgo, hecho='false')
#end def

def editar_riesgo(request, riesgo):
	modo = request.POST.get('modo', False)
	services = RiesgoService()
	riesgo, hecho = services.editar_riesgo(request, riesgo)
	if hecho:
		if   modo == 'h':
			return redirect(reverse(panel_riesgo, kwargs={}))
		elif modo == 's':
			return redirect(reverse(form_editar_riesgo, kwargs={'riesgo':riesgo.pk})+'?hecho=true')
		elif modo == 'm':
			return redirect(reverse(mostrar_riesgo, kwargs={'riesgo': riesgo.pk}))
		#end if
	#end if
	return form_editar_riesgo(request, riesgo.instance.pk, form=riesgo, hecho='false')
#end def

def panel_evaluacionriesgos(request, empresa):
	services = RiesgoService()
	empresa = services.mostrar_empresa(request, empresa)
	if empresa:
		evaluacionriesgoss = services.panel_evaluacionriesgos(request, empresa.pk)
		return render(request, 'riesgo/panel_evaluacionriesgos.html', {'evaluacionriesgoss':evaluacionriesgoss, 'empresa': empresa})
	#end if
	raise Http404
#end def

def mostrar_evaluacionriesgos(request, evaluacionriesgos):
	services = RiesgoService()
	evaluacionriesgos = services.mostrar_evaluacionriesgos(request, evaluacionriesgos)
	if evaluacionriesgos:
		return render(request, 'riesgo/mostrar_evaluacionriesgos.html',{'evaluacionriesgos':evaluacionriesgos})
	#end if
	raise Http404
#end def

def form_crear_evaluacionriesgos(request, empresa, formset=None, hecho=None):
	hecho = request.POST.get('hecho', hecho)
	services = RiesgoService()
	empresa, riesgos = services.mostrar_riesgos(request, empresa)
	if empresa:
		if not formset:
			formset = services.form_evaluacionriesgos(request, empresa.pk)
		#end if
		return render(request, 'riesgo/form_evaluacionriesgos.html', {'formset': formset, 'empresa':empresa, 'riesgos':riesgos, 'hecho': hecho})
	#end if
	raise Http404
#end def

def form_editar_evaluacionriesgos(request, evaluacionriesgos, form=None, hecho=None):
	hecho = request.POST.get('hecho', hecho)
	services = RiesgoService()
	riesgos, evaluacionriesgos = services.mostrar_evaluacionriesgos(request, evaluacionriesgos)
	if evaluacionriesgos:
		if not form:
			form = services.form_evaluacionriesgos(request, evaluacionriesgos)
		#end if
		return render(request, 'riesgo/form_evaluacionriesgos.html', {'evaluacionriesgos': evaluacionriesgos, 'riesgos':riesgos, 'form': form})
	#end if
	raise Http404
#end def

def crear_evaluacionriesgos(request):
	modo = request.POST.get('modo', False)
	empresa = request.POST.get('empresa', False)
	services = RiesgoService()
	empresa = services.mostrar_empresa(request, empresa)
	if empresa:
		evaluacionriesgos, hecho = services.crear_evaluacionriesgos(request, empresa)
		if hecho:
			return HttpResponse(status=201)
		#end if
	#end if
	return form_crear_evaluacionriesgos(request, empresa = empresa.pk, formset=evaluacionriesgos, hecho='false')
#end def

def editar_evaluacionriesgos(request, evaluacionriesgos):
	modo = request.POST.get('modo', False)
	services = RiesgoService()
	evaluacionriesgos, hecho = services.editar_evaluacionriesgos(request, evaluacionriesgos)
	if hecho:
		if   modo == 'h':
			return redirect(reverse(panel_evaluacionriesgos, kwargs={'empresa': evaluacionriesgos.empresa.pk}))
		elif modo == 's':
			return redirect(reverse(form_editar_evaluacionriesgos, kwargs={'evaluacionriesgos':evaluacionriesgos.pk})+'?hecho=true')
		elif modo == 'm':
			return redirect(reverse(mostrar_evaluacionriesgos, kwargs={'evaluacionriesgos': evaluacionriesgos.pk}))
		#end if
	#end if
	return form_editar_evaluacionriesgos(request, evaluacionriesgos.instance.pk, form=evaluacionriesgos, hecho='false')
#end def
