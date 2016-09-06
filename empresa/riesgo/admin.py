from huella.admin import admin_site
import models

admin_site.register(models.Criticidad)
admin_site.register(models.ElementoProteger)
admin_site.register(models.CargoRiesgo)
admin_site.register(models.Riesgo)
admin_site.register(models.EvaluacionRiesgos)
admin_site.register(models.EvaluacionEmpresa)
