from empresa.services import EmpresaService
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
def panel_empresas(obj):
	serivices = EmpresaService()
	empresas  = serivices.panel_empresa(())
	return empresas
#end def

