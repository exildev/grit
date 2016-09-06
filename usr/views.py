# -*- encoding: utf8 -*-
from django.shortcuts import render, redirect
from services import UsrService

def login(request):
	error = request.GET.get('error', '')
	return render(request, 'usr/login.html', {'error':error})
#end def

def login_do(request):
	usr = UsrService.get_instance()
	if usr.login(request):
		return redirect("/")
	#end if
	return redirect("/usr/login/?error=true")
#end def

def logout(request):
	usr = UsrService.get_instance()
	usr.logout(request)
	return redirect("/")
#end def

