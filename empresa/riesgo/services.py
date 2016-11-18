from models import Criticidad, ElementoProteger, CargoRiesgo, Riesgo, EvaluacionRiesgos, EvaluacionEmpresa
from forms import CriticidadForm, ElementoProtegerForm, CargoRiesgoForm, RiesgoForm, EvaluacionRiesgosFormSet
from django.db import connection
from django.db.models import Count
from empresa.services import EmpresaService
import json

class RiesgoService(EmpresaService):
	matriz = (
		('Bajo'    , 'Bajo'    , 'Moderado', 'Alto'   , 'Alto'   ),
		('Bajo'    , 'Bajo'    , 'Moderado', 'Alto'   , 'Extremo'),
		('Bajo'    , 'Moderado', 'Alto'    , 'Extremo', 'Extremo'),
		('Moderado', 'Alto'    , 'Alto'    , 'Extremo', 'Extremo'),
		('Alto'    , 'Alto'    , 'Extremo' , 'Extremo', 'Extremo')
	);


	def panel_criticidad(self, request):
		criticidads = Criticidad.objects.all()
		return criticidads
	#end def

	def mostrar_criticidad(sels, request, pk):
		criticidad = Criticidad.objects.filter(pk = pk).first()
		if criticidad:
			return criticidad
		#end if
		return False
	#end def

	def form_criticidad(self, request, criticidad = None):
		if request.POST:
			return CriticidadForm(request.POST, instance = criticidad)
		else:
			return CriticidadForm(instance = criticidad)
		#end if
	#end def

	def crear_criticidad(self, request):
		form = CriticidadForm(request.POST)
		if form.is_valid():
			criticidad = form.save()
			return criticidad, True
		#end if
		return form, False
	#end def

	def editar_criticidad(self, request, pk):
		criticidad = Criticidad.objects.filter(pk = pk).first()
		if criticidad:
			form = self.form_criticidad(request, criticidad)
			if form.is_valid():
				criticidad = form.save()
				return criticidad, True
			#end if
			return form, False
		#end if
		return None, False
	#end def

	def panel_elementoproteger(self, request):
		elementoprotegers = ElementoProteger.objects.all()
		return elementoprotegers
	#end def

	def mostrar_elementoproteger(sels, request, pk):
		elementoproteger = ElementoProteger.objects.filter(pk = pk).first()
		if elementoproteger:
			return elementoproteger
		#end if
		return False
	#end def

	def form_elementoproteger(self, request, elementoproteger = None):
		if request.POST:
			return ElementoProtegerForm(request.POST, instance = elementoproteger)
		else:
			return ElementoProtegerForm(instance = elementoproteger)
		#end if
	#end def

	def crear_elementoproteger(self, request):
		form = ElementoProtegerForm(request.POST)
		if form.is_valid():
			elementoproteger = form.save()
			return elementoproteger, True
		#end if
		return form, False
	#end def

	def editar_elementoproteger(self, request, pk):
		elementoproteger = ElementoProteger.objects.filter(pk = pk).first()
		if elementoproteger:
			form = self.form_elementoproteger(request, elementoproteger)
			if form.is_valid():
				elementoproteger = form.save()
				return elementoproteger, True
			#end if
			return form, False
		#end if
		return None, False
	#end def

	def panel_cargoriesgo(self, request):
		cargoriesgos = CargoRiesgo.objects.all()
		return cargoriesgos
	#end def

	def mostrar_cargoriesgo(sels, request, pk):
		cargoriesgo = CargoRiesgo.objects.filter(pk = pk).first()
		if cargoriesgo:
			return cargoriesgo
		#end if
		return False
	#end def

	def mostrar_cargoriesgo_cargo(sels, request, pk):
		cargoriesgo = CargoRiesgo.objects.filter(cargo__pk = pk).first()
		if cargoriesgo:
			return cargoriesgo
		#end if
		return False
	#end def

	def form_cargoriesgo(self, request, cargoriesgo = None):
		if request.POST:
			return CargoRiesgoForm(request.POST, instance = cargoriesgo)
		else:
			return CargoRiesgoForm(instance = cargoriesgo)
		#end if
	#end def

	def crear_cargoriesgo(self, request):
		form = CargoRiesgoForm(request.POST)
		if form.is_valid():
			cargoriesgo = form.save()
			return cargoriesgo, True
		#end if
		return form, False
	#end def

	def editar_cargoriesgo(self, request, pk):
		cargoriesgo = CargoRiesgo.objects.filter(pk = pk).first()
		if cargoriesgo:
			form = self.form_cargoriesgo(request, cargoriesgo)
			if form.is_valid():
				cargoriesgo = form.save()
				return cargoriesgo, True
			#end if
			return form, False
		#end if
		return None, False
	#end def

	def panel_riesgo(self, request):
		riesgos = Riesgo.objects.all()
		return riesgos
	#end def

	def mostrar_riesgo(sels, request, pk):
		riesgo = Riesgo.objects.filter(pk = pk).first()
		if riesgo:
			return riesgo
		#end if
		return False
	#end def

	def mostrar_riesgos(sels, request, empresa):
		empresa = EmpresaService().mostrar_empresa(request, empresa)
		if empresa:
			riesgos = Riesgo.objects.filter(empresa = empresa)
			return empresa, riesgos
		#end if
		return False, False
	#end def

	def form_riesgo(self, request, riesgo = None):
		if request.POST:
			return RiesgoForm(request.POST, instance = riesgo)
		else:
			return RiesgoForm(instance = riesgo)
		#end if
	#end def

	def crear_riesgo(self, request):
		form = RiesgoForm(request.POST)
		if form.is_valid():
			riesgo = form.save()
			return riesgo, True
		#end if
		return form, False
	#end def

	def editar_riesgo(self, request, pk):
		riesgo = Riesgo.objects.filter(pk = pk).first()
		if riesgo:
			form = self.form_riesgo(request, riesgo)
			if form.is_valid():
				riesgo = form.save()
				return riesgo, True
			#end if
			return form, False
		#end if
		return None, False
	#end def

	def panel_evaluacionriesgos(self, request, empresa):
		evaluacionriesgoss = EvaluacionRiesgos.objects.filter(empresa__pk = empresa)
		return evaluacionriesgoss
	#end def

	def mostrar_evaluacionriesgos(sels, request, pk):
		evaluacionriesgos = EvaluacionRiesgos.objects.filter(pk = pk).first()
		if evaluacionriesgos:
			riesgos = self.mostrar_riesgos(request, evaluacionriesgos.empresa.pk)
			return riesgos, evaluacionriesgos
		#end if
		return False
	#end def

	def form_evaluacionriesgos(self, request, empresa = None):
		if request.POST:
			return EvaluacionRiesgosFormSet(request.POST)
		else:
			initial = []
			riesgos = Riesgo.objects.filter(empresa = empresa)
			for riesgo in riesgos:
				initial.append({
					'riesgo': riesgo.pk
				})
			#end for
			return EvaluacionRiesgosFormSet(initial=initial)
		#end if
	#end def

	def crear_evaluacionriesgos(self, request, empresa):
		formset = self.form_evaluacionriesgos(request)
		if formset.is_valid():
			evaluacion = EvaluacionEmpresa(empresa = empresa)
			evaluacion.save()
			for form in formset:
				evaluacionriesgos = form.save(commit=False)
				evaluacionriesgos.empresa = evaluacion
				evaluacionriesgos.save()
			#end for
			return True, True
		#end if
		print formset.errors
		return formset, False
	#end def

	def editar_evaluacionriesgos(self, request, pk):
		evaluacionriesgos = EvaluacionRiesgos.objects.filter(pk = pk).first()
		if evaluacionriesgos:
			form = self.form_evaluacionriesgos(request, evaluacionriesgos)
			if form.is_valid():
				evaluacionriesgos = form.save()
				return evaluacionriesgos, True
			#end if
			return form, False
		#end if
		return None, False
	#end def
#end class