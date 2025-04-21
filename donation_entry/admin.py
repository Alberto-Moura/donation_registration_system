from django.contrib import admin
from .models import Donation_entry, DonatedItem
from django.utils.html import format_html
from django.urls import reverse


class DonatedItemInline(admin.TabularInline):
    model = DonatedItem
    extra = 1
    verbose_name = 'Item doado'
    verbose_name_plural = 'Itens doados'


@admin.register(Donation_entry)
class DonationEntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_of_contact', 'typesInstitution', 'name', 'created_at', 'updated_at')
    search_fields = ('id', 'date_of_contact', 'typesInstitution__type', 'name__name')
    list_filter = ('id', 'date_of_contact', 'typesInstitution', 'name')
    ordering = ('id', 'date_of_contact', 'name')
    list_per_page = 40
    inlines = [DonatedItemInline]


    class Media:
        js = (
            'donation_entry/js/institution_autofill.js',
            'donation_entry/js/institution_filter.js',
        )


@admin.register(DonatedItem)
class DonatedItemAdmin(admin.ModelAdmin):
    list_display = ('donation_id_link', 'entry_date', 'donor_name', 'item_name', 'quantity', 'acronym', 'category')
    search_fields = ('donation_entry__id', 'donation_entry__name__name', 'item_name__name')
    list_filter = ('donation_entry__date_of_contact', 'donation_entry__typesInstitution', 'category')
    ordering = ('-donation_entry__date_of_contact',)
    list_per_page = 40

    def donation_id_link(self, obj):
        url = reverse("admin:donation_entry_donation_entry_change", args=[obj.donation_entry.id])
        return format_html('<a href="{}">{}</a>', url, obj.donation_entry.id)
    donation_id_link.short_description = 'ID Entrada'
    donation_id_link.admin_order_field = 'donation_entry__id'

    def entry_date(self, obj):
        return obj.donation_entry.date_of_contact
    entry_date.short_description = 'Data Entrada'

    def donor_name(self, obj):
        return obj.donation_entry.name.name if obj.donation_entry.name else "ANÔNIMO"
    donor_name.short_description = 'Doador'