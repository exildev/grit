from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from exileui.admin import exileui
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    #url(r'^$', 'huella.views.index', name='index'),
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(exileui.urls)),
    #url(r'^empresa/', include('empresa.urls')),
    #url(r'^norma/', include('norma.urls')),
    #url(r'^notificacion/', include('notificacion.urls')),

    url(r'^nested_admin/', include('nested_admin.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
