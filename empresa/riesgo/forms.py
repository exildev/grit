from django import forms 
from django.forms.formsets import formset_factory
from models import Criticidad, ElementoProteger, CargoRiesgo, Riesgo, EvaluacionRiesgos
from empresa.models import Empresa

class CriticidadForm(forms.ModelForm):
	class Meta:
		exclude = ()
		model = Criticidad
	#end class
#end class

class ElementoProtegerForm(forms.ModelForm):
	class Meta:
		exclude = ()
		model = ElementoProteger
	#end class
#end class

class CargoRiesgoForm(forms.ModelForm):
	class Meta:
		exclude = ()
		model = CargoRiesgo
	#end class
#end class

class RiesgoForm(forms.ModelForm):
	class Meta:
		exclude = ()
		model = Riesgo
	#end class
#end class

class EvaluacionRiesgosForm(forms.ModelForm):
	riesgo = forms.ModelChoiceField(queryset=Riesgo.objects, widget=forms.HiddenInput())
	class Meta:
		exclude = ('empresa', )
		model = EvaluacionRiesgos
	#end class

	def riesgo_choices(self):
		return self.get_riesgo_display()
	#end def
#end class

EvaluacionRiesgosFormSet = formset_factory(EvaluacionRiesgosForm, extra=0)