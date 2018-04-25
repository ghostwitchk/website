from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Whole)
admin.site.register(models.Processor)
admin.site.register(models.Ram)
admin.site.register(models.Cart)