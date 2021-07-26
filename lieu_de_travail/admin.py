from django.contrib import admin
from . import models


admin.site.register(models.Province)
admin.site.register(models.Region)
admin.site.register(models.Commissariat_De_Police)
admin.site.register(models.Lieu_De_Travail)

