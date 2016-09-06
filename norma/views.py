"""from services import NormaService
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

def panel_norma(request):
	services = NormaService()
	normas = services.panel_norma(request)
	return render(request, 'norma/panel_norma.html', {'normas': normas})
#end def

def mostrar_norma(request, norma):
	services = NormaService()
	norma = services.mostrar_norma(request, norma)
	if norma:
		return render(request, 'norma/mostrar_norma.html', {'norma': norma})
	#end if
	raise Http404
#end def

def form_crear_norma(request, form=None, hecho=None):
	hecho = request.POST.get('hecho', hecho)
	services = NormaService()
	if not form:
		form = services.form_norma(request)
	#end if
	return render(request, 'norma/form_norma.html', {'form': form, 'hecho': hecho})
#end def

def form_editar_norma(request, norma, form=None, hecho=None):
	hecho = request.POST.get('hecho', hecho)
	services = NormaService()
	norma = services.mostrar_norma(request, norma)
	if norma:
		if not form:
			form = services.form_norma(request, norma)
		#end if
		return render(request, 'norma/form_norma.html', {'norma': norma, 'form': form})
	#end if
	raise Http404
#end def

def crear_norma(request):
	modo = request.POST.get('modo', False)
	services = NormaService()
	norma, hecho = services.crear_norma(request)
	if hecho:
		if   modo == 'h':
			return redirect(reverse(panel_norma))
		elif modo == 's':
			return redirect(reverse(form_crear_norma, kwargs={})+'?hecho=true')
		elif modo == 'm':
			return redirect(reverse(mostrar_norma, kwargs={'norma': norma.pk}))
		#end if
	#end if
	return form_crear_norma(request, form=norma, hecho='false')
#end def

def editar_norma(request, norma):
	modo = request.POST.get('modo', False)
	services = NormaService()
	norma, hecho = services.editar_norma(request, norma)
	if hecho:
		if   modo == 'h':
			return redirect(reverse(panel_norma))
		elif modo == 's':
			return redirect(reverse(form_editar_norma, kwargs={'norma': norma.pk})+'?hecho=true')
		elif modo == 'm':
			return redirect(reverse(mostrar_norma, kwargs={'norma': norma.pk}))
		#end if
	#end if
	return form_editar_norma(request, norma.instance.pk, form=norma, hecho='false')
#end def

def panel_item(request, norma):
	services = NormaService()
	norma = services.mostrar_norma(request, norma)
	if norma:
		items = services.panel_item(request, norma.pk)
		return render(request, 'norma/panel_item.html', {'items': items, 'norma': norma})
	#end if
	raise Http404
#end def

def mostrar_item(request, item):
	services = NormaService()
	item = services.mostrar_item(request, item)
	if item:
		return render(request, 'norma/mostrar_item.html', {'item': item})
	#end if
	raise Http404
#end def

def form_crear_item(request, norma, form=None, hecho=None):
	hecho = request.POST.get('hecho', hecho)
	services = NormaService()
	norma = services.mostrar_norma(request, norma)
	if norma:
		if not form:
			form = services.form_item(request)
		#end if
		return render(request, 'norma/form_item.html', {'form': form, 'norma': norma, 'hecho': hecho})
	#end if
	raise Http404
#end def

def form_editar_item(request, item, form=None, hecho=None):
	hecho = request.POST.get('hecho', hecho)
	services = NormaService()
	item = services.mostrar_item(request, item)
	if item:
		if not form:
			form = services.form_item(request, item)
		#end if
		return render(request, 'norma/form_item.html', {'item': item, 'form': form})
	#end if
	raise Http404
#end def

def crear_item(request):
	modo = request.POST.get('modo', False)
	services = NormaService()
	item, hecho = services.crear_item(request)
	if hecho:
		if   modo == 'h':
			return redirect(reverse(panel_item, kwargs={'norma': item.norma.pk}))
		elif modo == 's':
			return redirect(reverse(form_crear_item, kwargs={'norma': item.norma.pk})+'?hecho=true')
		elif modo == 'm':
			return redirect(reverse(mostrar_item, kwargs={'item': item.pk}))
		#end if
	#end if
	if item['norma'].value():
		return form_crear_item(request, item['norma'].value(), form=item, hecho='false')
	#end if
	raise Http404
#end def

def editar_item(request, item):
	modo = request.POST.get('modo', False)
	services = NormaService()
	item, hecho = services.editar_item(request, item)
	if hecho:
		if   modo == 'h':
			return redirect(reverse(panel_item, kwargs={'norma': item.norma.pk}))
		elif modo == 's':
			return redirect(reverse(form_editar_item, kwargs={'item': item.pk})+'?hecho=true')
		elif modo == 'm':
			return redirect(reverse(mostrar_item, kwargs={'item': item.pk}))
		#end if
	#end if
	return form_editar_item(request, item.instance.pk, form=item, hecho='false')
#end def

def panel_formato(request, item):
	services = NormaService()
	item = services.mostrar_item(request, item)
	if item:
		formatos = services.panel_formato(request, item.pk)
		return render(request, 'norma/panel_formato.html', {'formatos': formatos, 'item': item})
	#end if
	raise Http404
#end def

def mostrar_formato(request, formato):
	services = NormaService()
	formato = services.mostrar_formato(request, formato)
	if formato:
		return render(request, 'norma/mostrar_formato.html', {'formato': formato})
	#end if
	raise Http404
#end def

def form_crear_formato(request, item, form=None, hecho=None):
	hecho = request.POST.get('hecho', hecho)
	services = NormaService()
	item = services.mostrar_item(request, item)
	if item:
		if not form:
			form = services.form_formato(request)
		#end if
		return render(request, 'norma/form_formato.html', {'form': form, 'item': item,'hecho': hecho})
	#end if
	raise Http404
#end def

def form_editar_formato(request, formato, form=None, hecho=None):
	hecho = request.POST.get('hecho', hecho)
	services = NormaService()
	formato = services.mostrar_formato(request, formato)
	if formato:
		if not form:
			form = services.form_formato(request, formato)
		#end if
		return render(request, 'norma/form_formato.html', {'formato': formato, 'form': form})
	#end if
	raise Http404
#end def

def crear_formato(request):
	modo = request.POST.get('modo', False)
	item = request.POST.get('item', False)
	services = NormaService()
	formato, hecho = services.crear_formato(request)
	if hecho:
		if   modo == 'h':
			return redirect(reverse(panel_formato, kwargs={'item': formato.item.pk}))
		elif modo == 's':
			return redirect(reverse(form_crear_formato, kwargs={'item': formato.item.pk})+'?hecho=true')
		elif modo == 'm':
			return redirect(reverse(mostrar_formato, kwargs={'formato': formato.pk}))
		#end if
	#end if
	if item:
		return form_crear_formato(request, item, form=formato, hecho='false')
	#end if
	raise Http404
#end def

def editar_formato(request, formato):
	modo = request.POST.get('modo', False)
	services = NormaService()
	formato, hecho = services.editar_formato(request, formato)
	if hecho:
		if   modo == 'h':
			return redirect(reverse(panel_formato, kwargs={'item': formato.item.pk}))
		elif modo == 's':
			return redirect(reverse(form_editar_formato, kwargs={'formato': formato.pk})+'?hecho=true')
		elif modo == 'm':
			return redirect(reverse(mostrar_formato, kwargs={'formato': formato.pk}))
		#end if
	#end if
	return form_editar_formato(request, formato.instance.pk, form=formato, hecho='false')
#end def
"""