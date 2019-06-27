from django.contrib import admin
from . import models


admin.site.register(models.Account)             # Акаунты
admin.site.register(models.Parent)              # Родители