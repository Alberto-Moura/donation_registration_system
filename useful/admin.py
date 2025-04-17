from django.contrib import admin
from .models import Neighborhood, Crass


@admin.register(Neighborhood)
class NeighborhoodAdmin(admin.ModelAdmin):
    list_display = ('neighborhood', 'created_at', 'updated_at')
    search_fields = ('neighborhood',)
    list_filter = ('neighborhood',)
    ordering = ('neighborhood',)
    list_per_page = 20


@admin.register(Crass)
class CrassAdmin(admin.ModelAdmin):
    list_display = ('crassOrigin', 'name', 'created_at', 'updated_at')
    search_fields = ('crassOrigin', 'name')
    list_filter = ('crassOrigin', 'name')
    ordering = ('crassOrigin', 'name')
    list_per_page = 20
