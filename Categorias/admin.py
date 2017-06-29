from django.contrib import admin
from Categorias.models import Restaurantes, Esteticas, Hoteles, Veterinarias


admin.site.register(Restaurantes)
admin.site.register(Esteticas)
admin.site.register(Hoteles)
admin.site.register(Veterinarias)
