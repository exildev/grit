from django.conf.urls import patterns, url
from empresa.riesgo import views

urlpatterns = patterns('',
	#criticidad
	url(r'^panel/criticidad/$', views.panel_criticidad, name='panel_criticidad'),
	url(r'^form/editar/criticidad/(?P<criticidad>\d+)/$', views.form_editar_criticidad, name='form_editar_criticidad'),
	url(r'^form/crear/criticidad/$', views.form_crear_criticidad, name='form_crear_criticidad'),
	url(r'^crear/criticidad/$', views.crear_criticidad, name='crear_criticidad'),
	url(r'^editar/criticidad/(?P<criticidad>\d+)/$', views.editar_criticidad, name='editar_criticidad'),
	url(r'^mostrar/criticidad/(?P<criticidad>\d+)/$', views.mostrar_criticidad, name='mostrar_criticidad'),

	#elementoproteger
	url(r'^panel/elementoproteger/$', views.panel_elementoproteger, name='panel_elementoproteger'),
	url(r'^form/editar/elementoproteger/(?P<elementoproteger>\d+)/$', views.form_editar_elementoproteger, name='form_editar_elementoproteger'),
	url(r'^form/crear/elementoproteger/$', views.form_crear_elementoproteger, name='form_crear_elementoproteger'),
	url(r'^crear/elementoproteger/$', views.crear_elementoproteger, name='crear_elementoproteger'),
	url(r'^editar/elementoproteger/(?P<elementoproteger>\d+)/$', views.editar_elementoproteger, name='editar_elementoproteger'),
	url(r'^mostrar/elementoproteger/(?P<elementoproteger>\d+)/$', views.mostrar_elementoproteger, name='mostrar_elementoproteger'),

	#cargoriesgo
	url(r'^panel/cargoriesgo/$', views.panel_cargoriesgo, name='panel_cargoriesgo'),
	url(r'^form/editar/cargoriesgo/(?P<cargoriesgo>\d+)/$', views.form_editar_cargoriesgo, name='form_editar_cargoriesgo'),
	url(r'^form/crear/cargoriesgo/(?P<cargo>\d+)/$', views.form_crear_cargoriesgo, name='form_crear_cargoriesgo'),
	url(r'^crear/cargoriesgo/$', views.crear_cargoriesgo, name='crear_cargoriesgo'),
	url(r'^editar/cargoriesgo/(?P<cargoriesgo>\d+)/$', views.editar_cargoriesgo, name='editar_cargoriesgo'),
	url(r'^mostrar/cargoriesgo/(?P<cargo>\d+)/$', views.mostrar_cargoriesgo, name='mostrar_cargoriesgo'),

	#riesgo
	url(r'^panel/riesgo/$', views.panel_riesgo, name='panel_riesgo'),
	url(r'^form/editar/riesgo/(?P<riesgo>\d+)/$', views.form_editar_riesgo, name='form_editar_riesgo'),
	url(r'^form/crear/riesgo/$', views.form_crear_riesgo, name='form_crear_riesgo'),
	url(r'^crear/riesgo/$', views.crear_riesgo, name='crear_riesgo'),
	url(r'^editar/riesgo/(?P<riesgo>\d+)/$', views.editar_riesgo, name='editar_riesgo'),
	url(r'^mostrar/riesgo/(?P<riesgo>\d+)/$', views.mostrar_riesgo, name='mostrar_riesgo'),

	#evaluacionriesgos
	url(r'^panel/evaluacionriesgos/(?P<empresa>\d+)/$', views.panel_evaluacionriesgos, name='panel_evaluacionriesgos'),
	url(r'^form/editar/evaluacionriesgos/(?P<evaluacionriesgos>\d+)/$', views.form_editar_evaluacionriesgos, name='form_editar_evaluacionriesgos'),
	url(r'^form/crear/evaluacionriesgos/(?P<empresa>\d+)/$', views.form_crear_evaluacionriesgos, name='form_crear_evaluacionriesgos'),
	url(r'^crear/evaluacionriesgos/$', views.crear_evaluacionriesgos, name='crear_evaluacionriesgos'),
	url(r'^editar/evaluacionriesgos/(?P<evaluacionriesgos>\d+)/$', views.editar_evaluacionriesgos, name='editar_evaluacionriesgos'),
	url(r'^mostrar/evaluacionriesgos/(?P<evaluacionriesgos>\d+)/$', views.mostrar_evaluacionriesgos, name='mostrar_evaluacionriesgos'),

)