from django.contrib import admin
from .models import donation_entry


@admin.register(donation_entry)
class DonationEntryAdmin(admin.ModelAdmin):
    class Media:
        js = ('donation_entry/js/donation_entry.js',)
