from django.contrib import admin
from sitio.models import Noticia, Categoria


class AdminNoticia(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'fecha',)
    list_filter = ('archivada', 'fecha')
    search_fields = ('titulo', 'texto', )
    date_hierarchy = 'fecha'


admin.site.register(Noticia, AdminNoticia)
admin.site.register(Categoria)
