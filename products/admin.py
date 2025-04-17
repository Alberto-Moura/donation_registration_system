from django.contrib import admin
from .models import Category, Acronym, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Acronym)
class AcronymAdmin(admin.ModelAdmin):
    list_display = ('acronym', 'description', 'created_at', 'updated_at')
    list_filter = ('acronym',)
    search_fields = ('acronym',)
    ordering = ('acronym',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'compound_quantity', 'category', 'acronym', 'created_at', 'updated_at')
    list_filter = ('name', 'compound_quantity', 'category', 'acronym', 'created_at', 'updated_at')
    search_fields = ('name', 'compound_quantity', 'category', 'acronym')
    ordering = ('name', 'compound_quantity', 'category', 'acronym', 'created_at', 'updated_at')
    list_per_page = 20
