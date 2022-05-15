from django.contrib import admin
from .models import Service
# Aquí ponemos todo lo que queremos que sea visible para el admin

class ServiceAdmin(admin.ModelAdmin):
    readonly_fields= ('created', 'updated')

admin.site.register(Service, ServiceAdmin)
