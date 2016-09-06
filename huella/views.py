from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

def index(request):
	return render(request, 'huella/index.html', {})
#end def