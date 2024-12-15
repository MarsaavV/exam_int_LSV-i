from django.contrib import admin
from platos.models import Plato

@admin.register(Plato)
class PlatoAdmin(admin.ModelAdmin):
    list_display = ('precio',)
    list_filter = ('precio',)
    search_fields = ('procedencia',)
