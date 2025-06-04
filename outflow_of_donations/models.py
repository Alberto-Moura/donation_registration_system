from django.db import models
from useful.models import Neighborhood, Crass
from products.models import Product
from beneficiaries.models import Beneficiary, TypesBeneficiary


# Donation registration
class Donation_exit(models.Model):
    date_of_contact = models.DateField(
        verbose_name='Data de Contato ou Lançamento')
    type_beneficiary = models.ForeignKey(
        TypesBeneficiary,
        on_delete=models.PROTECT,
        related_name='type_beneficiary',
        verbose_name='Tipo de Beneficiário')
    name = models.ForeignKey(
        Beneficiary,
        on_delete=models.PROTECT,
        related_name='name_beneficiary',
        verbose_name='Nome do Beneficiário')
    document_id = models.CharField(
        max_length=15,
        verbose_name='Documento de Identificação')
    address = models.CharField(
        max_length=255,
        verbose_name='Endereço')
    number = models.CharField(
        max_length=10,
        verbose_name='Número')
    neighborhood = models.ForeignKey(
        Neighborhood,
        on_delete=models.PROTECT,
        verbose_name='Bairro')
    complement = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Complemento')
    phone_1 = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name='Telefone Principal')
    phone_2 = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name='Telefone Secundário')
    cras_origin = models.ForeignKey(
        Crass,
        on_delete=models.PROTECT,
        related_name='cras_origin',
        verbose_name='Cras Origem')
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
        ordering = ['date_of_contact']
        verbose_name = 'Saída de Doação'
        verbose_name_plural = 'Saídas de Doações'

    def __str__(self):
        ''''
        funcion to return a string representation of the Donation_exit instance.
        '''
        return f"{self.document_id} - {self.date_of_contact}"
    
    def clear(self):
        '''
        function to clear the Donation_exit instance.
        '''
        if self.address:
            self.address = self.address.upper()
        if self.observation:
            self.observation = self.observation.upper()
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class Donated_exit_item(models.Model):
    '''
    model to represent the items of the Donation_exit instance.
    '''
    donation_exit = models.ForeignKey(
        Donation_exit,
        on_delete=models.CASCADE,
        related_name='donated_exit_items',
        verbose_name='Saída de Doação')
    item_name = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name='product_exit',
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
        verbose_name = 'Saída de Doação - Itens'
        verbose_name_plural = 'Saídas de Doações - Itens'
