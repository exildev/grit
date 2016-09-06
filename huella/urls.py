from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from admin import admin_site
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^$', 'huella.views.index', name='index'),
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(admin_site.urls)),
    #url(r'^empresa/', include('empresa.urls')),
    #url(r'^norma/', include('norma.urls')),
    #url(r'^notificacion/', include('notificacion.urls')),
)


if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT
        })
    )
#end if
