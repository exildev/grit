from django.db import connection
from pydp import PyDP

import forms
import models
import json


class Service:

	def confirmar_validable_form(self, request):
		return forms.ConformarValidableForm()
	#end def

	def confirmar_validable(self, request):
		validable = request.GET.get('validable',False)
		single    = request.GET.get('single', False)

		validable = Validable.objects.filter(pk = validable).first()
		
		if validable:
			template = json.loads(unicode(validable.template.template))
			single   = json.loads(single)
			pydp = PyDP()
			pydp.init()
			valid = pydp.validate(pydp.DPFJ_FMD_DP_VER_FEATURES, single, pydp.DPFJ_FMD_DP_REG_FEATURES, template)
			if valid:
				return 201, valid
			#end i
			return 200, valid
		#end if
		return 400, False
	#end def

	def crear_validable(self, request):
		form = ValidableForm(request.POST)
		if form.is_valid():
			form.save()
			return 200, {"msg":"Guardado con exito"}
		#end if
		return 400, form.errors
	#end def

	def crear_template(self, request):
		form = TemplateForm(request.POST)
		if form.is_valid():
			form.save()
			return 200, {"msg":"Guardado con exito"}
		#end if
		return 400, form.errors
	#end def

#end class