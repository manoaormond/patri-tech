from django.contrib import admin
from .models import Unidade, Sala, Status, Bem

@admin.register(Unidade)
class UnidadeAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "endereco")
    search_fields = ("nome",)


@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "unidade")
    list_filter = ("unidade",)


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ("id", "nome")


@admin.register(Bem)
class BemAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "tombo", "unidade", "sala", "status")
    search_fields = ("nome", "tombo")
    list_filter = ("unidade", "sala", "status")

# Register your models here.
