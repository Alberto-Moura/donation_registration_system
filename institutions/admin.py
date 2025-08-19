from django.contrib import admin
from .models import TypesInstitution, Institution


@admin.register(TypesInstitution)
class TypesInstitutionAdmin(admin.ModelAdmin):
    list_display = ('type', 'created_at', 'updated_at')
    search_fields = ('type',)
    list_filter = ('type',)
    ordering = ('type',)
    list_per_page = 20


@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('name', 'cnpj', 'typesInstitution', 'address', 'number', 'phone', 'neighborhood', 'active', 'created_at', 'updated_at')
    search_fields = ('name', 'address', 'number', 'phone')
    list_filter = ('typesInstitution', 'name')
    ordering = ('name',)
    list_per_page = 20
