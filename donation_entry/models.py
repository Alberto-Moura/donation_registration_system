from django.db import models
from useful.models import Neighborhood, Crass
from django.core.exceptions import ValidationError
from beneficiaries.models import TypesBeneficiary, Beneficiary
from institutions.models import Institution, TypesInstitution


# Cadastro Instituições
class donation_entry(models.Model):
    date_of_contact = models.DateField(
        verbose_name='Data de Contato')
    withdrawal_date = models.DateField(
        blank=True,
        null=True,
        verbose_name='Data de Retirada')
    pick_up_time = models.TimeField(
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
        verbose_name='Nome do Doador')
    address = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Endereço do beneficiário')
    number = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        verbose_name='Número')
    phone_1 = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name='Telefone Principal')
    contact = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Contato')
    neighborhood = models.ForeignKey(
        Neighborhood,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        verbose_name='Bairro')
    crassOrigin = models.ForeignKey(
        Crass,
        on_delete=models.PROTECT,
        related_name='crass_origin',
        verbose_name='CRAS de Origem')
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
        ordering = ['name']
        verbose_name = 'Beneficiário'
        verbose_name_plural = 'Beneficiários'

    def __str__(self):
        return self.name

    def clean(self):
        self.cpf = self.cpf.replace('.', '').replace('-', '').replace('/', '')
        self.name = self.name.upper()
        self.address = self.address.upper()
        self.observation = self.observation.upper()

        if Beneficiary.objects.filter(cpf=self.cpf).exclude(pk=self.pk).exists():
            raise ValidationError({'name': 'Já existe um beneficiário com esse CPF.'})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)