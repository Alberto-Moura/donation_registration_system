from django.contrib import admin
from .models import TypesBeneficiary, Beneficiary


@admin.register(TypesBeneficiary)
class TypesBeneficiaryAdmin(admin.ModelAdmin):
    list_display = ('type', 'created_at', 'updated_at')
    search_fields = ('type',)
    list_filter = ('type',)
    ordering = ('type',)
    list_per_page = 20


@admin.register(Beneficiary)
class BeneficiaryAdmin(admin.ModelAdmin):
    list_display = ('name', 'cpf', 'typesBeneficiary', 'ethnicty', 'address', 'number', 'phone_1', 'phone_2', 'neighborhood', 'active', 'created_at', 'updated_at')
    search_fields = ('name', 'address', 'number', 'phone')
    list_filter = ('typesBeneficiary', 'name', 'address', 'neighborhood')
    ordering = ('name',)
    list_per_page = 20
