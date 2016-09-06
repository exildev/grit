from django.conf.urls import patterns, include, url
from notificacion import views
"""
urlpatterns = patterns('',

	url(r'^panel/recordatorio/(?P<notificable>\d+)/$', views.panel_recordatorio, name='panel_recordatorio'),
	url(r'^mostrar/recordatorio/(?P<recordatorio>\d+)/$', views.mostrar_recordatorio, name='mostrar_recordatorio'),
	url(r'^form/crear/recordatorio/(?P<notificable>\d+)/$', views.form_crear_recordatorio, name='form_crear_recordatorio'),
	url(r'^crear/recordatorio/(?P<notificable>\d+)/$', views.crear_recordatorio, name='crear_recordatorio'),
	url(r'^form/editar/recordatorio/(?P<recordatorio>\d+)/$', views.form_editar_recordatorio, name='form_editar_recordatorio'),
	url(r'^editar/recordatorio/(?P<recordatorio>\d+)/$', views.editar_recordatorio, name='editar_recordatorio'),
	url(r'^mostrar/avisos/(?P<recordable>\d+)/$', views.mostrar_avisos, name='mostrar_avisos'),
	url(r'^revisar/aviso/(?P<aviso>\d+)/$', views.revisar_aviso, name='revisar_aviso'),
)"""