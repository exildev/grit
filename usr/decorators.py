# -*- encoding: utf8 -*-
from django.shortcuts import redirect
from services import UsrService

def empresa(view):
	def func(request, *args, **kwargs):
		usr = UsrService.get_instance()
		if usr.es_empresa(request):
			return view(request, *args, **kwargs)
		else:
			return redirect("/")
		#end id
	#end def
	return func
#end def

def auditor(view):
	def func(request, *args, **kwargs):
		usr = UsrService.get_instance()
		if usr.es_auditor(request):
			return view(request, *args, **kwargs)
		else:
			return redirect("/")
		#end id
	#end def
	return func
#end def

def administrador(view):
	def func(request, *args, **kwargs):
		usr = UsrService.get_instance()
		if usr.es_administrador(request):
			return view(request, *args, **kwargs)
		else:
			return redirect("/")
		#end id
	#end def
	return func
#end def

def empleado(view):
	def func(request, *args, **kwargs):
		usr = UsrService.get_instance()
		if usr.es_empleado(request):
			return view(request, *args, **kwargs)
		else:
			return redirect("/")
		#end id
	#end def
	return func
#end def


def usuario(view):
	def func(request, *args, **kwargs):
		usr = UsrService.get_instance()
		if usr.es_usuario(request):
			return view(request, *args, **kwargs)
		else:
			return redirect("/")
		#end if
	#end def
	return func
#end def