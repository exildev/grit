from django.conf.urls import patterns, include, url
from empresa import views

urlpatterns = [
    url(r'^$', views.panel_departamento, name='inicio'),
    url(r'^riesgo/', include('empresa.riesgo.urls')),

    # test
    url(r'^test/empresa/$', views.test_empresa, name='test_empresa'),

    # empresa
    url(r'^json/empresa/$', views.json_empresa, name='json_empresa'),
    url(r'^panel/empresa/$', views.panel_empresa, name='panel_empresa'),
    url(r'^form/editar/empresa/(?P<empresa>\d+)/$',
        views.form_editar_empresa, name='form_editar_empresa'),
    url(r'^form/crear/empresa/$', views.form_crear_empresa,
        name='form_crear_empresa'),
    url(r'^crear/empresa/$', views.crear_empresa, name='crear_empresa'),
    url(r'^editar/empresa/(?P<empresa>\d+)/$',
        views.editar_empresa, name='editar_empresa'),
    url(r'^mostrar/empresa/(?P<empresa>\d+)/$',
        views.mostrar_empresa, name='mostrar_empresa'),

    # departamento
    url(r'^panel/departamento/(?P<empresa>\d+)/$',
        views.panel_departamento, name='panel_departamento'),
    url(r'^form/editar/departamento/(?P<departamento>\d+)/$',
        views.form_editar_departamento, name='form_editar_departamento'),
    url(r'^form/crear/departamento/(?P<empresa>\d+)/$',
        views.form_crear_departamento, name='form_crear_departamento'),
    url(r'^crear/departamento/$', views.crear_departamento,
        name='crear_departamento'),
    url(r'^editar/departamento/(?P<departamento>\d+)/$',
        views.editar_departamento, name='editar_departamento'),
    url(r'^mostrar/departamento/(?P<departamento>\d+)/$',
        views.mostrar_departamento, name='mostrar_departamento'),

    # cargo
    url(r'^panel/cargo/(?P<departamento>\d+)/$',
        views.panel_cargo, name='panel_cargo'),
    url(r'^json/cargo/$', views.json_cargo, name='json_cargo'),
    url(r'^form/editar/cargo/(?P<cargo>\d+)/$',
        views.form_editar_cargo, name='form_editar_cargo'),
    url(r'^form/crear/cargo/(?P<departamento>\d+)/$',
        views.form_crear_cargo, name='form_crear_cargo'),
    url(r'^crear/cargo/$', views.crear_cargo, name='crear_cargo'),
    url(r'^editar/cargo/(?P<cargo>\d+)/$',
        views.editar_cargo, name='editar_cargo'),
    url(r'^mostrar/cargo/(?P<cargo>\d+)/$',
        views.mostrar_cargo, name='mostrar_cargo'),

    # requesito
    url(r'^form/crear/requisito/(?P<cargo>\d+)/$',
        views.form_crear_requisito, name='form_crear_requisito'),
    url(r'^form/editar/requisito/(?P<cargo>\d+)/$',
        views.form_editar_requisito, name='form_editar_requisito'),
    url(r'^crear/requisito/(?P<cargo>\d+)/$',
        views.crear_requisito, name='crear_requisito'),
    url(r'^editar/requisito/(?P<cargo>\d+)/$',
        views.editar_requisito, name='editar_requisito'),

    # empleado
    url(r'^panel/empleado/(?P<cargo>\d+)/$',
        views.panel_empleado, name='panel_empleado'),
    url(r'^form/editar/empleado/(?P<empleado>\d+)/$',
        views.form_editar_empleado, name='form_editar_empleado'),
    url(r'^form/crear/empleado/(?P<cargo>\d+)/$',
        views.form_crear_empleado, name='form_crear_empleado'),
    url(r'^crear/empleado/$', views.crear_empleado, name='crear_empleado'),
    url(r'^editar/empleado/(?P<empleado>\d+)/$',
        views.editar_empleado, name='editar_empleado'),
    url(r'^mostrar/empleado/(?P<empleado>\d+)/$',
        views.mostrar_empleado, name='mostrar_empleado'),

    # jefes
    url(r'^crear/jefes/$', views.crear_jefes, name='crear_jefes'),
    url(r'^editar/jefes/(?P<departamento>\d+)/$',
        views.editar_jefes, name='editar_jefes'),


]
