from django.db import models
from useful.models import Neighborhood, Crass
from django.core.exceptions import ValidationError


# Tipos de Instituições
class TypesBeneficiary(models.Model):
    type = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Tipo de Beneficiário')
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
        ordering = ['type']
        verbose_name = 'Tipo de Beneficiário'
        verbose_name_plural = 'Tipos de Beneficiários'

    def __str__(self):
        return self.type

    def clean(self):
        self.type = self.type.upper()
        self.observation = self.observation.upper()

        if TypesBeneficiary.objects.filter(type=self.type).exclude(pk=self.pk).exists():
            raise ValidationError({'type': 'Já existe um tipo de beneficiário com esse nome.'})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


# Cadastro Instituições
class Beneficiary(models.Model):
    typesBeneficiary = models.ForeignKey(
        TypesBeneficiary,
        on_delete=models.PROTECT,
        related_name='typebeneficiary',
        verbose_name='Tipo de beneficiário')
    name = models.CharField(
        max_length=255,
        verbose_name='Nome do beneficiário')
    cpf = models.CharField(
        max_length=15,
        unique=True,
        verbose_name='CPF')
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
    phone_2 = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name='Telefone Secundário')
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
        verbose_name='CRASS de Origem')
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
