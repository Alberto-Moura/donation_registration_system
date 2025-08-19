from django.contrib import admin
from .models import Donation_entry, DonatedItem, DonationDisposal
from django.utils.html import format_html
from django.urls import reverse
from django.http import HttpResponseRedirect


class DonatedItemInline(admin.TabularInline):
    model = DonatedItem
    extra = 0
    exclude = ('product_acronym', 'product_category')
    verbose_name = 'Item Doado'
    verbose_name_plural = 'Itens Doados'

    def product_acronym(self, obj):
        return obj.item_name.acronym
    product_acronym.short_description = 'Unidade'

    def product_category(self, obj):
        return obj.item_name.category
    product_category.short_description = 'Categoria'


class DonatedDisposalInline(admin.TabularInline):
    model = DonationDisposal
    extra = 0
    exclude = ('product_acronym', 'product_category')
    verbose_name = 'Item Descartado'
    verbose_name_plural = 'Itens Descartados'

    def product_acronym(self, obj):
        return obj.item_name.acronym
    product_acronym.short_description = 'Unidade'

    def product_category(self, obj):
        return obj.item_name.category
    product_category.short_description = 'Categoria'


@admin.register(Donation_entry)
class DonationEntryAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    fields = (
        'id',
        'registration_number', 
        'type_donation',
        'date_of_contact',
        'withdrawal_date',
        'pick_up_time',
        'typesInstitution',
        'name',
        'address',
        'number',
        'neighborhood',
        'phone',
        'contact',
        'observation',
    )

    list_display = ('id', 'registration_number', 'type_donation', 'date_of_contact', 'typesInstitution', 'name', 'created_at', 'updated_at')
    search_fields = ('id', 'registration_number', 'type_donation', 'date_of_contact', 'typesInstitution__type', 'name__name')
    list_filter = ('id', 'registration_number', 'type_donation', 'date_of_contact', 'typesInstitution', 'name')
    ordering = ('-id', 'date_of_contact', 'name')
    list_per_page = 40
    inlines = [DonatedItemInline, DonatedDisposalInline]

    class Media:
        css = {
            'all': ('donation_entry/css/admin_custom.css',)
        }
        js = (
            'donation_entry/js/institution_autofill.js',
            'donation_entry/js/institution_filter.js',
            'donation_entry/js/move_add_button.js',
            'donation_entry/js/product_autofill.js',
            'donation_entry/js/toggle_inlines.js',
        )


@admin.register(DonatedItem)
class DonatedItemAdmin(admin.ModelAdmin):
    list_display = ('donation_id', 'date_of_contact', 'donor_name', 'item_name', 'quantity', 'product_acronym', 'product_category')
    list_select_related = ('donation_entry', 'item_name')
    search_fields = ('donation_entry__id', 'donation_entry__name__name', 'item_name__name')
    list_filter = ('donation_entry__date_of_contact', 'donation_entry__typesInstitution')
    ordering = ('-donation_entry__date_of_contact',)
    list_per_page = 40

    @admin.display(description="Unidade")
    def product_acronym(self, obj):
        return obj.item_name.acronym

    @admin.display(description="Categoria")
    def product_category(self, obj):
        return obj.item_name.category

    def donation_id(self, obj):
        url = reverse("admin:donation_entry_donation_entry_change", args=[obj.donation_entry.id])
        return format_html('<a href="{}">{}</a>', url, obj.donation_entry.id)
    donation_id.short_description = 'ID Entrada'
    donation_id.admin_order_field = 'donation_entry__id'

    def donor_name(self, obj):
        return obj.donation_entry.name.name if obj.donation_entry.name else 'ANÔNIMO'
    donor_name.short_description = 'Doador'
    donor_name.admin_order_field = 'donation_entry__name__name'

    def date_of_contact(self, obj):
        return obj.donation_entry.date_of_contact
    date_of_contact.short_description = 'Data Entrada'
    date_of_contact.admin_order_field = 'donation_entry__date_of_contact'

    def add_view(self, request, form_url='', extra_context=None):
        return HttpResponseRedirect(reverse('admin:donation_entry_donation_entry_add'))

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['title'] = 'Visualização de Itens por Entrada'
        return super().changelist_view(request, extra_context=extra_context)


@admin.register(DonationDisposal)
class DonatedDisposalAdmin(admin.ModelAdmin):
    list_display = ('donation_id', 'date_of_contact', 'donor_name', 'item_name', 'quantity', 'product_acronym', 'product_category')
    list_select_related = ('donation_entry', 'item_name')
    search_fields = ('donation_entry__id', 'donation_entry__name__name', 'item_name__name')
    list_filter = ('donation_entry__date_of_contact', 'donation_entry__typesInstitution')
    ordering = ('-donation_entry__date_of_contact',)
    list_per_page = 40

    @admin.display(description="Unidade")
    def product_acronym(self, obj):
        return obj.item_name.acronym

    @admin.display(description="Categoria")
    def product_category(self, obj):
        return obj.item_name.category

    def donation_id(self, obj):
        url = reverse("admin:donation_entry_donation_entry_change", args=[obj.donation_entry.id])
        return format_html('<a href="{}">{}</a>', url, obj.donation_entry.id)
    donation_id.short_description = 'ID Descarte'
    donation_id.admin_order_field = 'donation_entry__id'

    def donor_name(self, obj):
        return obj.donation_entry.name.name if obj.donation_entry.name else 'ANÔNIMO'
    donor_name.short_description = 'Doador'
    donor_name.admin_order_field = 'donation_entry__name__name'

    def date_of_contact(self, obj):
        return obj.donation_entry.date_of_contact
    date_of_contact.short_description = 'Data Entrada'
    date_of_contact.admin_order_field = 'donation_entry__date_of_contact'

    def add_view(self, request, form_url='', extra_context=None):
        return HttpResponseRedirect(reverse('admin:donation_entry_donation_entry_add'))

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['title'] = 'Visualização de Itens Descartados'
        return super().changelist_view(request, extra_context=extra_context)
