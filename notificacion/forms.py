"""from django import forms 

class PeriodicidadForm(forms.ModelForm):
	class Meta:
		model = Periodicidad
		exclude = ()
	#end class
#end class

class RecordatorioForm(forms.ModelForm):
	class Meta:
		model = Recordatorio
		exclude = ('periodicidad', )
	#end class
#end class

class RecordatorioEditarForm(forms.ModelForm):
	periodo = forms.BooleanField(initial=False, required=False)
	class Meta:
		model = Recordatorio
		exclude = ('fecha', 'periodicidad', 'url', )
	#end class
#end class

class PeriodoForm(forms.ModelForm):
	class Meta:
		model = Periodo
		exclude = ()
	#end class
#end class

class NotificableForm(forms.ModelForm):
	class Meta:
		model = Notificable
		exclude = ()
	#end class
#end class

class RecordableForm(forms.ModelForm):
	class Meta:
		model = Recordable
		exclude = ()
	#end class
#end class

class RevisionForm(forms.ModelForm):
	class Meta:
		model = Revision
		exclude = ()
	#end class
#end class
"""