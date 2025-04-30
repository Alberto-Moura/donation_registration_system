from django.db import models
from useful.models import Neighborhood
from institutions.models import Institution, TypesInstitution
from products.models import Product


def is_anon_type(typesInstitution):
    return typesInstitution and typesInstitution.type.upper() == "ANÔNIMO"


# Cadastro Instituições
class Donation_entry(models.Model):
    OPTIONS_TYPE_DONATION = [
        ("ENTRADA", "ENTRADA"),
        ("DESCARTE", "DESCARTE"),
        ("INVENTÁRIO", "INVENTÁRIO"),
    ]
    OPTIONS_TIME_WITHDRAWAL = [
        ("PERÍODO DA MANHÃ", "PERÍODO DA MANHÃ"),
        ("PERÍODO DA TARDE", "PERÍODO DA TARDE"),
        ("07:00", "07:00"),
        ("08:00", "08:00"),
        ("09:00", "09:00"),
        ("10:00", "10:00"),
        ("11:00", "11:00"),
        ("12:00", "12:00"),
        ("13:00", "13:00"),
        ("14:00", "14:00"),
        ("15:00", "15:00"),
        ("16:00", "16:00"),
        ("17:00", "17:00"),
        ("18:00", "18:00"),
    ]
    type_donation = models.CharField(
        max_length=20,
        choices=OPTIONS_TYPE_DONATION,
        verbose_name='Tipo de Lançamento',
        default='ENTRADA')
    date_of_contact = models.DateField(
        verbose_name='Data de Contato ou Lançamento')
    withdrawal_date = models.DateField(
        blank=True,
        null=True,
        verbose_name='Data de Retirada (Opcional)')
    pick_up_time = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        choices=OPTIONS_TIME_WITHDRAWAL,
        verbose_name='Hora de Retirada')
    typesInstitution = models.ForeignKey(
        TypesInstitution,
        on_delete=models.PROTECT,
        related_name='typesinstitution',
        verbose_name='Tipo de Doador')
    name = models.ForeignKey(
        Institution,
        on_delete=models.PROTECT,
        related_name='institution',
        verbose_name='Nome do Doador',
        null=True,
        blank=True)
    address = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Endereço')
    number = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        verbose_name='Número')
    neighborhood = models.ForeignKey(
        Neighborhood,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        verbose_name='Bairro')
    phone = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name='Telefone')
    contact = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Contato')
    observation = models.TextField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Observação')
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data de Criação')
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Data de Atualização')

    class Meta:
        ordering = ['id']
        verbose_name = 'Cadastrar Entrada'
        verbose_name_plural = 'Cadastrar Entradas'

    def __str__(self):
        return str(self.name) if self.name else "ANÔNIMO"

    def clean(self):
        if self.address:
            self.address = self.address.upper()
        if self.contact:
            self.contact = self.contact.upper()
        if self.observation:
            self.observation = self.observation.upper()

    def save_related(self, request, form, formsets, change):
        if is_anon_type(self.typesInstitution):
            self.name = None
            if not self.address:
                self.address = None
            if not self.phone:
                self.phone = None
            if not self.contact:
                self.contact = None
            if not self.number:
                self.number = None
            if not self.neighborhood:
                self.neighborhood = None

        super().save_related(request, form, formsets, change)

        # A lógica de exclusão de inlines vai aqui:
        instance = form.instance
        if instance.type_donation == 'DESCARTE':
            instance.donated_items.all().delete()
        elif instance.type_donation == 'INVENTÁRIO':
            instance.disposal_item.all().delete()


class DonatedItem(models.Model):
    donation_entry = models.ForeignKey(
        Donation_entry,
        on_delete=models.CASCADE,
        related_name='donated_items',
        verbose_name='Entrada de Doação')
    item_name = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name='product',
        verbose_name='Nome do Item')
    quantity = models.PositiveBigIntegerField(
        verbose_name='Quantidade')
    observation = models.TextField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Observação')

    class Meta:
        ordering = ['id']
        verbose_name = 'Cadastrar Entrada'
        verbose_name_plural = 'Relatório de Entradas'

    def __str__(self):
        return f"{self.quantity} x {self.item_name}"


class DonationDisposal(models.Model):
    donation_entry = models.ForeignKey(
        Donation_entry,
        on_delete=models.CASCADE,
        related_name='disposal_item',
        verbose_name='Descarte de Doação')
    item_name = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name='disposal_product',
        verbose_name='Nome do Item')
    quantity = models.PositiveBigIntegerField(
        verbose_name='Quantidade')
    observation = models.TextField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Observação')

    class Meta:
        ordering = ['id']
        verbose_name = 'Cadastrar Entrada'
        verbose_name_plural = 'Descartes de Doações'

    def __str__(self):
        return f"{self.quantity} x {self.item_name}"
