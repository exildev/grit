from django.conf.urls import patterns, include, url
from norma import views
"""
urlpatterns = patterns('',
	url(r'^formulario/', include('norma.formulario.urls')),

	url(r'^$', views.panel_norma, name='panel_norma'),
	url(r'^form/editar/norma/(?P<norma>\d+)/$', views.form_editar_norma, name='form_editar_norma'),
	url(r'^form/crear/norma/$', views.form_crear_norma, name='form_crear_norma'),
	url(r'^crear/norma/$', views.crear_norma, name='crear_norma'),
	url(r'^editar/norma/(?P<norma>\d+)/$', views.editar_norma, name='editar_norma'),
	url(r'^mostrar/norma/(?P<norma>\d+)/$', views.mostrar_norma, name='mostrar_norma'),

	url(r'^panel/item/(?P<norma>\d+)/$', views.panel_item, name='panel_item'),
	url(r'^form/editar/item/(?P<item>\d+)/$', views.form_editar_item, name='form_editar_item'),
	url(r'^form/crear/item/(?P<norma>\d+)/$', views.form_crear_item, name='form_crear_item'),
	url(r'^crear/item/$', views.crear_item, name='crear_item'),
	url(r'^editar/item/(?P<item>\d+)/$', views.editar_item, name='editar_item'),
	url(r'^mostrar/item/(?P<item>\d+)/$', views.mostrar_item, name='mostrar_item'),

	url(r'^panel/formato/(?P<item>\d+)/$', views.panel_formato, name='panel_formato'),
	url(r'^form/editar/formato/(?P<formato>\d+)/$', views.form_editar_formato, name='form_editar_formato'),
	url(r'^form/crear/formato/(?P<item>\d+)/$', views.form_crear_formato, name='form_crear_formato'),
	url(r'^crear/formato/$', views.crear_formato, name='crear_formato'),
	url(r'^editar/formato/(?P<formato>\d+)/$', views.editar_formato, name='editar_formato'),
	url(r'^mostrar/formato/(?P<formato>\d+)/$', views.mostrar_formato, name='mostrar_formato'),

)"""