from django.contrib import admin
from comensal.models import Comensal

@admin.register(Comensal)
class ComensalAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
