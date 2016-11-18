"""from django.shortcuts import render, redirect
from services import FormularioService
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from notificacion.models import Aviso

def form_crear_registro(request, formulario, form = None):
	aviso = request.GET.get('aviso', False)
	services = FormularioService()
	if not form:
		form = services.form_registro(request, formulario, extra=(('aviso', aviso, Aviso), ))
	#end if
	return render(request, 'formulario/form_crear_registro.html', {'form':form})
#end def

def crear_registro(request):
	aviso = request.POST.get('aviso', False)
	services = FormularioService()
	registro, formulario, hecho = services.crear_registro(request, extra=(('aviso', aviso, Aviso), ))
	if hecho:
		return HttpResponse(status=201)
	#end if
	return form_crear_registro(request, formulario.pk, registro)
#end def

def mostrar_registro(request, registro):
	services = FormularioService()
	registro, entradas = services.mostrar_registro(request, registro)
	if registro:
		return render(request, 'formulario/mostrar_registro.html', {'registro': registro, 'entradas': entradas})
	#end if
	raise Http404
#end def"""