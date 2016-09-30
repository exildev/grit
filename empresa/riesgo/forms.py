from django import forms 
from django.forms.formsets import formset_factory
from models import Criticidad, ElementoProteger, CargoRiesgo, Riesgo, EvaluacionRiesgos, EvaluacionEmpresa
from empresa.models import Empresa
import widgets
from django.db.models.signals import post_save
from django.dispatch import receiver

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
	#riesgo = forms.ModelChoiceField(queryset=Riesgo.objects, widget=forms.HiddenInput())
	class Meta:
		exclude = ('empresa', )
		model = EvaluacionRiesgos
		widgets = {
			'fuente': widgets.TextWidget,
			'medio': widgets.TextWidget,
			'persona': widgets.TextWidget,
			'metodo': widgets.TextWidget,
			'controles_administrativos': widgets.TextWidget,
			'controles_operacionales': widgets.TextWidget,
			'controles_talentoHumano': widgets.TextWidget,
			'controles_instalacion': widgets.TextWidget,
		}
	#end class

	def riesgo_choices(self):
		return self.get_riesgo_display()
	#end def
#end class

class EvaluacionEmpresaForm(forms.ModelForm):
	class Meta:
		model = EvaluacionEmpresa
		exclude = []
	#end class

	
# end class

@receiver(post_save, sender=EvaluacionEmpresa, dispatch_uid="post_save_evaliacion_empresa")
def post_save_evaliacion_empresa(sender, instance, **kwargs):
	riesgos = Riesgo.objects.filter(empresa=instance.empresa)
	if kwargs['created']:
		for riesgo in riesgos:
			EvaluacionRiesgos(empresa=instance, riesgo=riesgo).save()
		# end for
	# end if
# end def

EvaluacionRiesgosFormSet = formset_factory(EvaluacionRiesgosForm, extra=0)