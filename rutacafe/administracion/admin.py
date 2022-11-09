from django.contrib import admin

from .models import Emprendedor,Empredimiento,Clientes,Administrador

admin.site.register(Emprendedor)
admin.site.register(Empredimiento)
admin.site.register(Clientes)
admin.site.register(Administrador)

# Register your models here.
