from django.contrib import admin
from meseros.models import Mesero

@admin.register(Mesero)
class MeseroAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
