"""from models import Norma, Item, Formato
from forms import NormaForm, ItemForm, FormatoForm
from django.core.urlresolvers import reverse
from norma.formulario.services import FormularioService

class NormaService():
	def panel_norma(self, request):
		normas = Norma.objects.all()
		return normas
	#end def

	def mostrar_norma(self, request, pk):
		norma = Norma.objects.filter(pk = pk).first()
		if norma:
			return norma
		#end if
		return False
	#end def

	def form_norma(self, request, norma=None):
		if request.POST:
			return NormaForm(request.POST, instance = norma)
		else:
			return NormaForm(instance = norma)
		#end if
	#end def

	def crear_norma(self, request):
		form = NormaForm(request.POST)
		if form.is_valid():
			norma = form.save()
			return norma, True
		#end if
		return form, False
	#end def

	def editar_norma(self, request, pk):
		norma = Norma.objects.filter(pk = pk).first()
		if norma:
			form = self.form_norma(request, norma)
			if form.is_valid():
				norma = form.save()
				return norma, True
			#end if
			return form, False
		#end if
		return None, False
	#end def

	def panel_item(self, request, norma):
		items = Item.objects.filter(norma__pk = norma)
		return items
	#end def

	def mostrar_item(self, request, pk):
		item = Item.objects.filter(pk = pk).first()
		if item:
			return item
		#end if
		return False
	#end def

	def form_item(self, request, item=None):
		if request.POST:
			return ItemForm(request.POST, instance = item)
		else:
			return ItemForm(instance = item)
		#end if
	#end def

	def crear_item(self, request):
		form = ItemForm(request.POST)
		if form.is_valid():
			item = form.save()
			return item, True
		#end if
		return form, False
	#end def

	def editar_item(self, request, pk):
		item = Item.objects.filter(pk = pk).first()
		if item:
			form = self.form_item(request, item)
			if form.is_valid():
				item = form.save()
				return item, True
			#end if
			return form, False
		#end if
		return None, False
	#end def

	def panel_formato(self, request, item):
		formatos = Formato.objects.filter(item__pk = item)
		return formatos
	#end def

	def mostrar_formato(self, request, pk):
		formato = Formato.objects.filter(pk = pk).first()
		if formato:
			return formato
		#end if
		return False
	#end def

	def form_formato(self, request, formato=None):
		if request.POST:
			return FormatoForm(request.POST, instance = formato)
		else:
			return FormatoForm(instance = formato)
		#end if
	#end def

	def crear_formato(self, request):
		form = FormatoForm(request.POST)
		if form.is_valid():
			formato = form.save(commit=False)
			formato.url = ''
			formato.titulo = formato.nombre
			formato.save()
			formulario = formato.formulario
			if formulario:
				formato.url = reverse('form_crear_registro', kwargs={'formulario':formulario.pk})
			#end if
			formato.save()
			return formato, True
		#end if
		return form, False
	#end def

	def editar_formato(self, request, pk):
		formato = Formato.objects.filter(pk = pk).first()
		if formato:
			form = self.form_formato(request, formato)
			if form.is_valid():
				formato = form.save(commit=False)
				formato.url = ''
				formato.titulo = formato.nombre
				formato.save()
				formulario = formato.formulario
				if formulario:
					formato.url = reverse('form_crear_registro', kwargs={'formulario':formulario.pk})
				#end if
				formato.save()
				return formato, True
			#end if
			print form.errors
			return form, False
		#end if
		return None, False
	#end def

#end class"""