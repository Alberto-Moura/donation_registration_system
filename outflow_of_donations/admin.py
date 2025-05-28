from django.contrib import admin
from .models import Donated_exit_item, Donation_exit
from django.utils.html import format_html
from django.urls import reverse
from django.http import HttpResponseRedirect


class Donated_item_exit_inline(admin.TabularInline):
    model = Donated_exit_item
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


@admin.register(Donation_exit)
class Donation_exit_admin(admin.ModelAdmin):
    readonly_fields = ('id',)
    fields = (
        'id',
        'date_of_contact',
        'type_beneficiary',
        'name',
        'document_id',
        'address',
        'number',
        'neighborhood',
        'phone_1',
        'phone_2',
        'cras_origin',
        'observation',
    )

    list_display = ('id', 'date_of_contact', 'type_beneficiary', 'name', 'document_id', 'created_at', 'updated_at')
    search_fields = ('id', 'date_of_contact', 'name__name', 'document_id__cpf')
    list_filter = ('id', 'date_of_contact', 'name')
    ordering = ('-id', 'date_of_contact', 'name')
    list_per_page = 40
    inlines = [Donated_item_exit_inline]

    class Media:
        css = {
            # 'all': ('donation_entry/css/admin_custom.css',)
        }
        js = (
            # 'donation_entry/js/institution_autofill.js',
            # 'donation_entry/js/institution_filter.js',
            # 'donation_entry/js/move_add_button.js',
            # 'donation_entry/js/product_autofill.js',
            # 'donation_entry/js/toggle_inlines.js',
        )


@admin.register(Donated_exit_item)
class Donated_item_exit_admin(admin.ModelAdmin):
    list_display = ('donation_id', 'date_of_contact', 'donor_name', 'item_name', 'quantity', 'product_acronym', 'product_category')
    list_select_related = ('donation_exit', 'item_name')
    search_fields = ('donation_exit__id', 'donation_exit__name__name', 'item_name__name')
    list_filter = ('donation_exit__date_of_contact',)
    ordering = ('-donation_exit__date_of_contact',)
    list_per_page = 40

    @admin.display(description="Unidade")
    def product_acronym(self, obj):
        return obj.item_name.acronym

    @admin.display(description="Categoria")
    def product_category(self, obj):
        return obj.item_name.category

    def donation_id(self, obj):
        url = reverse("admin:donation_exit_donation_exit_change", args=[obj.donation_exit.id])
        return format_html('<a href="{}">{}</a>', url, obj.donation_exit.id)
    donation_id.short_description = 'ID Saída'
    donation_id.admin_order_field = 'donation_exit_id'

    def donor_name(self, obj):
        return obj.donation_exit.name.name if obj.donation_exit.name else 'ANÔNIMO'
    donor_name.short_description = 'Recebedor'
    donor_name.admin_order_field = 'donation_exit__name__name'

    def date_of_contact(self, obj):
        return obj.donation_exit.date_of_contact
    date_of_contact.short_description = 'Data Saída'
    date_of_contact.admin_order_field = 'donation_exit__date_of_contact'

    def add_view(self, request, form_url='', extra_context=None):
        return HttpResponseRedirect(reverse('admin:donation_exit_donation_exit_add'))

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['title'] = 'Visualização de Itens por Saída'
        return super().changelist_view(request, extra_context=extra_context)