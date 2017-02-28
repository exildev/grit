from django import forms 
from models import Valor, Formulario, Entrada, Tipo, Campo, Registro
from datetime import datetime
from django.contrib.admin import widgets
import re
import types
import unicodedata
import urllib, json


class FormularioForm(forms.ModelForm):
	class Meta:
		model = Formulario
		exclude = ()
	#end class
#end class

class CampoForm(forms.ModelForm):
	class Meta:
		model = Campo
		exclude = ()
	#end class
#end class


class Clean:
	def __init__(self, campo):
		self.campo = campo
	#end def

	def __call__(self, clean):
		nombre = self.remove_accents(clean.campo.nombre)
		valor = self.data[nombre]
		tipo  = clean.campo.tipo
		if tipo.regular:
			if regular.startswith("http://") or  regular.startswith("https://"):
				response = urllib.urlopen(regular+"?id="+valor)
				data = json.loads(response.read())
				return len(data) > 0
			# end if 
			if not re.match(tipo.regular, valor):
				raise forms.ValidationError("El campo debe ser de tipo %s" % (tipo,))
			#end if
		#end if
	#end def
#end class

class RegistroCreateForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(RegistroCreateForm, self).__init__(*args, **kwargs)

	class Meta:
		model = Registro
		exclude = ('completado',  'fecha')
	#end class
#end class

class RegistroEditForm(forms.ModelForm):
	@staticmethod
	def make(obj):
		campos = Campo.objects.filter(grupo__formulario = obj.formulario)
		fields = {}

		for campo in campos:
			nombre = RegistroEditForm.remove_accents(campo.nombre)
			fields[nombre] = RegistroEditForm.crear_campo(campo.tipo.forma, campo.nombre, RegistroEditForm.remove_accents(campo.grupo.nombre), campo.ver_como, campo.tipo.regular)
			def clean(self):
				return Clean(campo)
			#end def
			fields['clean_%s' % (nombre, )] = clean
		#end for

		def __init__(self, *args, **kwargs):
			super(RegistroEditForm, self).__init__(*args, **kwargs)
			campos = Campo.objects.filter(grupo__formulario = self.instance.formulario)
			for campo in campos:
				nombre = RegistroEditForm.remove_accents(campo.nombre)
				valor = Valor.objects.filter(entrada__registro=self.instance, entrada__campo = campo).first()
				if valor:
					self.initial[nombre] = str(valor)
				#end if
			#end def
		#end def

		fields['__init__'] = __init__

		return type("RegistroEditFormI", (RegistroEditForm, ), fields)
	#end def

	def __init__(self, *args, **kwargs):
		super(RegistroEditForm, self).__init__(*args, **kwargs)
		for campo in Campo.objects.filter(formulario = self.instance.formulario):
			nombre = self.remove_accents(campo.nombre)
			self.fields[nombre] = self.crear_campo(campo.tipo.forma, campo.nombre, RegistroEditForm.remove_accents(campo.grupo.nombre), campo.ver_como, campo.tipo.regular)
			valor = Valor.objects.filter(entrada__registro=self.instance, entrada__campo = campo).first()
			if valor:
				self.initial[nombre] = str(valor)
			#end if
			setattr(self, 'clean_%s' % (nombre, ), types.MethodType(Clean(campo), self))
		#end for
	#end def

	class Meta:
		model = Registro
		exclude = ('formulario', 'empleado', 'completado', 'fecha', 'revisor')
	#end class

	@staticmethod
	def remove_accents(data):
		return (''.join((c for c in unicodedata.normalize('NFD', data) if unicodedata.category(c) != 'Mn'))).replace(" ", "_")
	#end def

	@staticmethod
	def crear_campo(forma, label, grupo, ver_como, regular=''):
		forma = Tipo.FORMAS[forma][1]
		if   forma == 'Binario':
			field = forms.CharField(label = label, widget=forms.Textarea(), required=False, )
			field.widget = forms.TextInput(attrs = {"group": grupo, "ver": ver_como})
		elif forma == 'Decimal':
			field = forms.FloatField(label = label, required=False, )
			field.widget = forms.TextInput(attrs = {"group": grupo, "ver": ver_como})
		elif forma == 'Entero':
			field = forms.IntegerField(label = label, required=False, )
			field.widget = forms.TextInput(attrs = {"group": grupo, "ver": ver_como})
		elif forma == 'Cadena':
			field = forms.CharField(label = label, required=False, )
			field.widget = forms.TextInput(attrs = {"group": grupo, "ver": ver_como})
		elif forma == 'Parrafo':
			field = forms.CharField(label = label,  required=False, )
			field.widget = forms.Textarea(attrs = {"group": grupo, "ver": ver_como})
		elif forma == 'Fecha':
			field = forms.DateField(label = label, required=False, )
			field.widget = widgets.AdminDateWiget(attrs = {"group": grupo, "ver": ver_como})
		elif forma == 'Hora':
			field = forms.TimeField(label = label, required=False, )
			field.widget = forms.AdminTimeWiget(attrs = {"group": grupo, "ver": ver_como})
		elif forma == 'Fecha/Hora':
			field = forms.DateTimeField(label = label, required=False, )
			field.widget = forms.AdminSplitDateTimeWiget(attrs = {"group": grupo, "ver": ver_como})
		elif forma == 'Opciones':
			options = regular.replace('(', '').replace(')', '').split('|')
			CHOICES = ((i, options[i]) for i in range(len(options)))
			field = forms.IntegerField(label = label, choices=CHOICES)
		elif forma == 'Referencia':
			response = urllib.urlopen(regular)
			options = json.loads(response.read())
			CHOICES = ((o.id, o.value) for io in options)
			field = forms.IntegerField(label = label, choices=CHOICES)
		#end if
		return field
	#end def

	def save(self, commit=False):
		registro = super(RegistroEditForm, self).save(commit=False)
		registro.completado = True
		registro.fecha = datetime.now()
		registro.save()
		for campo in Campo.objects.filter(grupo__formulario = self.instance.formulario):
			nombre = self.remove_accents(campo.nombre)
			valor = self.data[nombre]
			if valor != None:
				tipo  = campo.tipo
				entrada, created = Entrada.objects.get_or_create(campo=campo, registro=registro)
				if created:
					valor = Valor(valor=valor, tipo=tipo)
					valor.save()
					entrada.valor = valor			
				else:
					entrada.valor.valor=valor
					entrada.valor.save()
				#end if
				entrada.save()
			# end if
		#end for
		return registro
	#end def

#end class
