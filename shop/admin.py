from django.contrib import admin
from shop.models import producto, categoria

admin.site.register(producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock', 'orden')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('precio', 'stock')
    ordering = ('orden',)

admin.site.register(categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre', 'descripcion')
    filter_horizontal = ('productos',)
    ordering = ('nombre',)