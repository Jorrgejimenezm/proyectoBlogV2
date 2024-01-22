from django.contrib import admin
from .models import Articulo, Comentario, Categoria

# Register your models here.
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ("id","titulo","texto","imagen","creado","modificado")

admin.site.register(Articulo, ArticuloAdmin)

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ("id","texto","articulo","creado","modificado")

admin.site.register(Comentario, ComentarioAdmin)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("id","nombre","descripcion","creado","modificado")

admin.site.register(Categoria, CategoriaAdmin)
