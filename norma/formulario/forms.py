from django import forms 
from models import Valor, Formulario, Entrada, Tipo, Campo, Registro
from datetime import datetime
import re
import types
import unicodedata


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
		campos = Campo.objects.filter(formulario = obj.formulario)
		fields = {}

		for campo in campos:
			nombre = RegistroEditForm.remove_accents(campo.nombre)
			fields[nombre] = RegistroEditForm.crear_campo(campo.tipo.forma, campo.nombre)
			def clean(self):
				return Clean(campo)
			#end def
			fields['clean_%s' % (nombre, )] = clean
		#end for

		def __init__(self, *args, **kwargs):
			super(RegistroEditForm, self).__init__(*args, **kwargs)
			campos = Campo.objects.filter(formulario = self.instance.formulario)
			for campo in campos:
				nombre = RegistroEditForm.remove_accents(campo.nombre)
				valor = Valor.objects.filter(entrada__registro=self.instance, entrada__campo = campo).first()
				if valor:
					print valor
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
			self.fields[nombre] = self.crear_campo(campo.tipo.forma, campo.nombre)
			valor = Valor.objects.filter(entrada__registro=self.instance, entrada__campo = campo).first()
			if valor:
				self.initial[nombre] = str(valor)
			#end if
			setattr(self, 'clean_%s' % (nombre, ), types.MethodType(Clean(campo), self))
		#end for
	#end def

	class Meta:
		model = Registro
		exclude = ('formulario', 'empleado', 'completado', 'fecha')
	#end class

	@staticmethod
	def remove_accents(data):
		return (''.join((c for c in unicodedata.normalize('NFD', data) if unicodedata.category(c) != 'Mn')))
	#end def

	@staticmethod
	def crear_campo(forma, label):
		forma = Tipo.FORMAS[forma][1]
		if   forma == 'Binario':
			return forms.CharField(label = label, widget=forms.Textarea())
		elif forma == 'Decimal':
			return forms.FloatField(label = label, )
		elif forma == 'Entero':
			return forms.IntegerField(label = label, )
		elif forma == 'Cadena':
			return forms.CharField(label = label, )
		elif forma == 'Parrafo':
			return forms.CharField(label = label, widget=forms.Textarea())
		elif forma == 'Fecha':
			return forms.DateField(label = label, )
		elif forma == 'Hora':
			return forms.TimeField(label = label, )
		elif forma == 'Fecha/Hora':
			return forms.DateTimeField(label = label, )
		#end if
	#end def

	def save(self, commit=False):
		registro = super(RegistroEditForm, self).save(commit=False)
		registro.completado = True
		registro.fecha = datetime.now()
		registro.save()
		for campo in Campo.objects.filter(formulario = self.instance.formulario):
			nombre = self.remove_accents(campo.nombre)
			valor = self.data[nombre]
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
		#end for
		return registro
	#end def

#end class
