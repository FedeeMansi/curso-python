from django.contrib import admin
from .models import Credenciales_P, Productos, random_pwd, Credenciales_DB, Contactarnos 


# Register your models here.
admin.site.register(Productos)
admin.site.register(Credenciales_P)
admin.site.register(Credenciales_DB)
admin.site.register(random_pwd)
admin.site.register(Contactarnos)