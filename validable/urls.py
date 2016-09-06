from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('validable/',
    url(r'^confirmar/validable/form/$', views.confirmar_validable_form, name='confirmar_validable_form'),
    url(r'^confirmar/validable/$', views.confirmar_validable, name='confirmar_validable'),
)