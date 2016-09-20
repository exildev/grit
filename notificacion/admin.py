from exile_ui.admin import admin_site
from django.contrib import admin
from models import Recordatorio, Periodicidad, Aviso, Revision

admin_site.register(Recordatorio)
admin_site.register(Periodicidad)
admin_site.register(Aviso)
admin_site.register(Revision)