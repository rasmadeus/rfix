from django.contrib import admin
from rfix.task import models


admin.site.register(models.Priority)
admin.site.register(models.State)
admin.site.register(models.Type)
