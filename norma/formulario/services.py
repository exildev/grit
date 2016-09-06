"""from norma.formulario.models import Tipo, Campo, Formulario, Registro, Valor, Entrada
from forms import RegistroForm
from notificacion.services import NotificacionService

class FormularioService:
	def mostrar_formulario(self, request, pk):
		formulario = Formulario.objects.filter(pk = pk).first()
		if formulario:
			return formulario
		#end if
		return False
	#end def

	def form_formulario(self, request):
		return ValorForm()
	#end def

	def form_registro(self, request, formulario, extra):
		formulario = Formulario.objects.filter(pk = formulario).first()
		if formulario:
			return RegistroForm(formulario = formulario, extra=extra)
		#end def
		return False
	#end def

	def crear_registro(self, request, extra):
		formulario = request.POST.get('formulario', False)
		if formulario:
			formulario = Formulario.objects.filter(pk = formulario).first()
			form = RegistroForm(formulario, extra,request.POST)
			if form.is_valid():
				registro = form.save()
				return registro, formulario, True
			#end def
			print form.errors, form.is_valid()
			return form, formulario, False
		#end if
		return None, None, False
	#end def

	def mostrar_registro(self, request, pk):
		registro = Registro.objects.filter(pk = pk).first()
		if registro:
			entradas = Entrada.objects.filter(registro__pk = pk)
			return registro, entradas
		#end if
		return False, False
	#end def
#end class"""