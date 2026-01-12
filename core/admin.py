from django.contrib import admin
from .models import Categoria, Status, Unidade, Sala, Bem

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')

@admin.register(Unidade)
class UnidadeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'codigo')

@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'unidade')

@admin.register(Bem)
class BemAdmin(admin.ModelAdmin):
    # Aqui usamos exatamente os nomes dos campos que estão no models.py
    list_display = ('tombo', 'nome', 'categoria', 'status', 'unidade', 'sala')
    list_filter = ('categoria', 'status', 'unidade')
    search_fields = ('tombo', 'nome')