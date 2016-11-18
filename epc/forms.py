<<<<<<< HEAD
from django.contrib.auth.forms import UserCreationForm
from django import forms 
from exile_ui.widgets import DatePickerWidget
import models
import widgets
from datetime import datetime
from usr.models import Empleado as EmpleadoU
from norma.formulario.models import Registro
from django.core.exceptions import ValidationError


class OrdenTrabajoForm(forms.ModelForm):
	class Meta:
		model = models.OrdenTrabajo
		exclude = []
		widgets = {
            #"fecha": DatePickerWidget(attrs={'class': 'date'}),
            #"dependencias": widgets.DependenceWidget()
        }
    # end class

	def clean(self):
		if self.cleaned_data['personal'] == self.cleaned_data['revisor']:
			raise ValidationError('El personal y el revisor no pueden ser iguales')
		# end if
		return self.cleaned_data
	# end def
# end class

class ActividadForm(forms.ModelForm):
	class Meta:
		model = models.Actividad
		exclude = ['registro']
		widgets = {
			'poscicion': widgets.OrdenableWidget()
        }
	#end class

	def save(self, commit=True):
		obj = super(ActividadForm, self).save(commit)
		if obj.completado and not obj.fecha_completado:
			obj.fecha_completado = datetime.now()
		# end if
		if obj.formato and obj.orden.personal.empleado:
			user = EmpleadoU.objects.filter(_empleado=obj.orden.personal.empleado).first()
			if user:
				registro = Registro(formulario=obj.formato, empleado=user)
				registro.save()
				obj.registro = registro
			# end if
		# end if
		obj.save()
		return obj
	# end def

# end class


class ActividadUserForm(forms.ModelForm):
	class Meta:
		model = models.Actividad
		exclude = ['formato', 'poscicion']
	#end class

	def __init__(self, *args, **kwargs):
		super(ActividadUserForm, self).__init__(*args, **kwargs)
		self.fields['registro'].widget = widgets.FillFormatWidget()
	# end def

	def save(self, commit=True):
		obj = super(ActividadUserForm, self).save(commit)
		if obj.completado and not obj.fecha_completado:
			obj.fecha_completado = datetime.now()
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

=======
from django.contrib.auth.forms import UserCreationForm
from django import forms 
from exileui.widgets import DatePickerWidget
import models
import widgets
from datetime import datetime
from usr.models import Empleado as EmpleadoU
from norma.formulario.models import Registro


class OrdenTrabajoForm(forms.ModelForm):
	class Meta:
		model = models.OrdenTrabajo
		exclude = []
		widgets = {
            "fecha": DatePickerWidget(attrs={'class': 'date'}),
            "dependencias": widgets.DependenceWidget()
        }
    # end class
# end class

class ActividadForm(forms.ModelForm):
	class Meta:
		model = models.Actividad
		exclude = ['registro']
		widgets = {
			'poscicion': widgets.OrdenableWidget()
        }
	#end class

	def save(self, commit=True):
		obj = super(ActividadForm, self).save(commit)
		if obj.completado and not obj.fecha_completado:
			obj.fecha_completado = datetime.now()
		# end if
		if obj.formato and obj.orden.personal.empleado:
			user = EmpleadoU.objects.filter(_empleado=obj.orden.personal.empleado).first()
			if user:
				registro = Registro(formulario=obj.formato, empleado=user)
				registro.save()
				obj.registro = registro
			# end if
		# end if
		obj.save()
		return obj
	# end def

# end class


class ActividadUserForm(forms.ModelForm):
	class Meta:
		model = models.Actividad
		exclude = ['formato', 'poscicion']
		widgets = {
			'registro': widgets.FillFormatWidget()
		}
	#end class

	def save(self, commit=True):
		obj = super(ActividadForm, self).save(commit)
		if obj.completado and not obj.fecha_completado:
			obj.fecha_completado = datetime.now()
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

>>>>>>> d4a43d94c0aa6b0b9855c268cd630ce06cd3af9c
# end class