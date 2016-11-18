from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

import services

@csrf_exempt
def confirmar_validable_form(request):
	service = services.Service()
	form = service.confirmar_validable_form(request)
	return render(request, 'validable/confirmar_validable.html', {'form': form})
#end def

@csrf_exempt
def confirmar_validable(request):
	service = services.Service()
	status, resp = service.confirmar_validable(request)
	return HttpResponse(resp, status = status)
#end def