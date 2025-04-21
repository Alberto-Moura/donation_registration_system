from django.contrib import admin
from .models import donation_entry


@admin.register(donation_entry)
class DonationEntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_of_contact', 'typesInstitution', 'name', 'created_at', 'updated_at')
    search_fields = ('id', 'date_of_contact', 'typesInstitution__type', 'name__name')
    list_filter = ('id', 'date_of_contact', 'typesInstitution', 'name')
    ordering = ('id', 'date_of_contact', 'name')
    list_per_page = 40

    class Media:
        js = ('donation_entry/js/institution_autofill.js',)
