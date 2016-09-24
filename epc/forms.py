from django.contrib.auth.forms import UserCreationForm
from django import forms 
from exile_ui.widgets import DatePickerWidget
import models
import widgets
from datetime import datetime


class OrdenTrabajoForm(forms.ModelForm):
	class Meta:
		model = models.OrdenTrabajo
		exclude = []
		widgets = {
            "fecha": DatePickerWidget(attrs={'class': 'date'})
        }
    # end class
# end class

class ActividadForm(forms.ModelForm):
	class Meta:
		model = models.Actividad
		exclude = []
		widgets = {
            "fecha_estimada": DatePickerWidget(attrs={'class': 'date'})
        }
	#end class

	def save(self, commit=True):
		obj = super(ActividadForm, self).save(commit)
		if obj.completado:
			obj.fecha_completado = datetime.now()
		else:
			obj.fecha_completado = None
		# end if
		obj.save()
		return obj
	# end def

# end class

class ProgresoGraficoForm(forms.ModelForm):
	grafica = forms.CharField()

	def __init__(self, *args, **kwargs):
		super(ProgresoGraficoForm, self).__init__(*args, **kwargs)
		if self.instance.pk:
			self.fields['grafica'].widget = widgets.LinearWidget(self.instance.orden)
		# en
	#end def

	class Meta:
		model = models.ProgresoGrafico
		exclude = []
	#end class

# end class

class GanttForm(forms.ModelForm):
	grafica = forms.CharField()

	def __init__(self, *args, **kwargs):
		super(GanttForm, self).__init__(*args, **kwargs)
		if self.instance.pk:
			self.fields['grafica'].widget = widgets.GanttWidget(self.instance.proyecto)
		# en
	#end def

	class Meta:
		model = models.Gantt
		exclude = []
	#end class

# end class