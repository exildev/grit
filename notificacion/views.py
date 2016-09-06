"""from services import NotificacionService
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

def panel_recordatorio(request, notificable):
	services = NotificacionService()
	notificable = services.mostrar_notificable(request, notificable)
	if notificable:
		recordatorios = services.panel_recordatorio(request, notificable.pk)
		return render(request, 'notificacion/panel_recordatorio.html', {'recordatorios': recordatorios})
	#end if
	raise Http404
#end def

def mostrar_recordatorio(request, recordatorio):
	services = NotificacionService()
	recordatorio, notificables = services.mostrar_recordatorio(request, recordatorio)
	if recordatorio:
		return render(request, 'notificacion/mostrar_recordatorio.html', {'recordatorio': recordatorio, 'notificables':notificables})
	#end if
	raise Http404
#end def

def form_crear_recordatorio(request, notificable, form=None, form_periodicidad=None, hecho=None):
	hecho = request.POST.get('hecho', hecho)
	services = NotificacionService()
	notificable = services.mostrar_notificable(request, notificable)
	if notificable:
		if not form:
			form, form_periodicidad = services.form_crear_recordatorio(request)
		#end if
		return render(request, 'notificacion/form_recordatorio.html', {'form': form, 'form_periodicidad':form_periodicidad, 'notificable':notificable, 'hecho': hecho})
	#end if
	raise Http404
#end def

def crear_recordatorio(request, notificable):
	modo = request.POST.get('modo', False)
	services = NotificacionService()
	recordatorio, periodicidad, hecho = services.crear_recordatorio(request, notificable)
	if hecho:
		if   modo == 'h':
			return redirect(reverse(panel_recordatorio, kwargs={'notificable':notificable}))
		elif modo == 's':
			return redirect(reverse(form_crear_recordatorio, kwargs={'notificable':notificable})+'?hecho=true')
		elif modo == 'm':
			return redirect(reverse(mostrar_recordatorio, kwargs={'recordatorio': recordatorio.pk}))
		#end if
	#end if
	return form_crear_recordatorio(request, notificable, form=recordatorio, form_periodicidad=periodicidad, hecho='false')
#end def

def form_editar_recordatorio(request, recordatorio, form=None, hecho=None):
	hecho = request.POST.get('hecho', hecho)
	services = NotificacionService()
	recordatorio, notificables = services.mostrar_recordatorio(request, recordatorio)
	if recordatorio:
		if not form:
			form = services.form_editar_recordatorio(request, recordatorio)
		#end if
		return render(request, 'notificacion/form_recordatorio.html', {'recordatorio': recordatorio, 'form': form})
	#end if
	raise Http404
#end def

def editar_recordatorio(request, recordatorio):
	modo = request.POST.get('modo', False)
	services = NotificacionService()
	recordatorio, periodicidad, hecho = services.editar_recordatorio(request, recordatorio)
	if hecho:
		return HttpResponse(status=201)
	#end if
	return form_editar_recordatorio(request, recordatorio.pk, form=periodicidad, hecho='false')
#end def

def mostrar_avisos(request, recordable):
	services = NotificacionService()
	recordable = services.mostrar_recordable(request, recordable)
	if recordable:
		avisos = services.mostrar_avisos_json(request, recordable.pk)
		return HttpResponse(avisos, content_type='application/json')
		#return render(request, 'notificacion/mostrar_avisos.html', {'avisos':avisos})
	#end if
	raise Http404
#end def

def revisar_aviso(request, aviso):
	services = NotificacionService()
	aviso = services.mostrar_aviso(request, aviso)
	if aviso:
		reviso = services.revisar_aviso(request, aviso)
		return HttpResponse()
	#end if
	raise Http404
#end def"""