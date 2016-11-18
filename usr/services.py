# -*- encoding: utf8 -*-
from django.contrib.auth import authenticate, login, logout
from models import Empresa, Auditor, Administrador, Empleado

class UsrService():
	instance = None

	@staticmethod
	def get_instance():
		if UsrService.instance == None:
			UsrService.instance = UsrService()
		#end if
		return UsrService.instance
	#end def

	def login(self, request):
		username = request.POST.get('username', '')
		password = request.POST.get('password', '')
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return True
			#end if
		#end if
		return False
	#end def

	def logout(self, request):
		logout(request)
		return True
	#end def

	def es_usuario(self, request):
		if request.user.is_authenticated():
			return True
		#end if
		return False
	#end def

	def es_empresa(self, request):
		if self.es_usuario(request):
			empresa = Empresa.objects.filter(usuario = request.user).first()
			if empresa:
				return empresa
			#end if
		#end if
		return False
	#end def

	def es_auditor(self, request):
		if self.es_usuario(request):
			auditor = Auditor.objects.filter(usuario = request.user).first()
			if auditor:
				return auditor
			#end if
		#end if
		return False
	#end def

	def es_administrador(self, request):
		if self.es_usuario(request):
			administrador = Administrador.objects.filter(usuario = request.user).first()
			if administrador:
				return administrador
			#end if
		#end if
		return False
	#end def

	def es_empleado(self, request):
		if self.es_usuario(request):
			empleado = Empleado.objects.filter(usuario = request.user).first()
			if empleado:
				return empleado
			#end if
		#end if
		return False
	#end def


#end class