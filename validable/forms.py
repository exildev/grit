from models import Validable, Template, Excusa
from django import forms

class ConfirmarValidableForm(forms.Form):
	validable = forms.TextField()
	single	  = forms.TextField()
#end class

class ValidableForm(forms.ModelForm):
	class Meta:
		model = Validable
		exclude = ('identificador','class_name')
	#end class
#end class

class TemplateForm(forms.ModelForm):
	class Meta:
		model = Template
	#end class
#end class