from django.db import models
from useful.models import Neighborhood, Crass
from django.core.exceptions import ValidationError
from validate_docbr import CPF


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
            raise ValidationError({'Tipo': 'Já existe esse tipo de beneficiário cadastrado.'})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


# Etnia
class TypesEthnicity(models.Model):
    type = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Raça/Etnia')
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
        verbose_name = 'Raça/Etnia'
        verbose_name_plural = 'Raças/Etnias'

    def __str__(self):
        return self.type

    def clean(self):
        self.type = self.type.upper()
        self.observation = self.observation.upper()

        if TypesBeneficiary.objects.filter(type=self.type).exclude(pk=self.pk).exists():
            raise ValidationError({'Raça/Etinia': 'Já existe essa raça e/ou etnia cadastrada.'})

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
    ethnicty = models.ForeignKey(
        TypesEthnicity,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        verbose_name='Raça/Etnia')
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
    active = models.BooleanField(
        default=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Beneficiário'
        verbose_name_plural = 'Beneficiários'

    def __str__(self):
        return self.name

    def clean(self):
        self.cpf = self.cpf.replace('.', '').replace('-', '').replace('/', '')
        self.name = self.name.upper()
        if self.address:
            self.address = self.address.upper()
        if self.observation:
            self.observation = self.observation.upper()

        if Beneficiary.objects.filter(cpf=self.cpf).exclude(pk=self.pk).exists():
            raise ValidationError({'Nome': 'Já existe um beneficiário com esse CPF.'})

        cpf_validator = CPF()
        if not cpf_validator.validate(self.cpf):
            raise ValidationError({'CPF': 'CPF inválido. Verifique e tente novamente.'})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
