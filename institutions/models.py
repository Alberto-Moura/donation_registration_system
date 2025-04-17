from django.db import models
from useful.models import Neighborhood
from django.core.exceptions import ValidationError


# Tipos de Instituições
class TypesInstitution(models.Model):
    type = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Tipo de Instituição')
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
        verbose_name = 'Tipo de Instituição'
        verbose_name_plural = 'Tipos de Instituições'

    def __str__(self):
        return self.type

    def clean(self):
        self.type = self.type.upper()
        self.observation = self.observation.upper()

        if TypesInstitution.objects.filter(type=self.type).exclude(pk=self.pk).exists():
            raise ValidationError({'type': 'Já existe um tipo de instituição com esse nome.'})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


# Cadastro Instituições
class Institution(models.Model):
    typesInstitution = models.ForeignKey(
        TypesInstitution,
        on_delete=models.PROTECT,
        related_name='typesInstitution',
        verbose_name='Tipo de Instituição')
    name = models.CharField(
        max_length=100,
        verbose_name='Nome da Instituição')
    cnpj = models.CharField(
        max_length=15,
        unique=True,
        blank=True,
        null=True,
        verbose_name='CNPJ')
    address = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Endereço da Instituição')
    number = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        verbose_name='Número')
    neighborhood = models.ForeignKey(
        Neighborhood,
        on_delete=models.PROTECT,
        verbose_name='Bairro')
    email = models.EmailField(
        max_length=255,
        unique=True,
        blank=True,
        null=True,
        verbose_name='Email')
    phone = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name='Telefone')
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data de Criação')
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Data de Atualização')

    class Meta:
        ordering = ['name']
        verbose_name = 'Instituição'
        verbose_name_plural = 'Instituições'

    def __str__(self):
        return self.name

    def clean(self):
        self.name = self.name.upper()
        self.address = self.address.upper()

        if Institution.objects.filter(name=self.name).exclude(pk=self.pk).exists():
            raise ValidationError({'name': 'Já existe uma instituição com esse nome.'})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
