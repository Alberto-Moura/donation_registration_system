from django.db import models
from useful.models import Neighborhood
from django.core.exceptions import ValidationError


# Tipos de Instituições
class TypesInstitution(models.Model):
    type = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Tipo')
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
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'

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
        verbose_name='Tipo')
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
        verbose_name='Endereço')
    number = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        verbose_name='Número')
    neighborhood = models.ForeignKey(
        Neighborhood,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Bairro')
    contact = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Contato')
    complement = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Complemento')
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
        verbose_name = 'Cadastrar'
        verbose_name_plural = 'Cadastrar'

    def __str__(self):
        return self.name

    def clean(self):
        if self.name:
            self.name = self.name.upper()
        if self.address:
            self.address = self.address.upper()
        if self.contact:
            self.contact = self.contact.upper()

        if Institution.objects.filter(name=self.name).exclude(pk=self.pk).exists():
            raise ValidationError({'name': 'Já existe uma instituição com esse nome.'})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
