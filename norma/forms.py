from django import forms 
from models import Norma, Item, Formato
from datetime import datetime

class NormaForm(forms.ModelForm):
	class Meta:
		model = Norma
		exclude = ('fecha_edicion',)
	#end class
	def save(self, commit=True):
		obj = super(NormaForm, self).save(commit)
		obj.fecha_edicion = datetime.now()
		obj.save()
		return obj
	#end if
#end class

class ItemForm(forms.ModelForm):
	class Meta:
		model = Item
		exclude = ()
	#end class
#end class

class FormatoForm(forms.ModelForm):
	class Meta:
		model = Formato
		exclude = ()
	#end class
#end class
