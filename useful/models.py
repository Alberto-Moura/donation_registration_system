from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


# Cadastro dos Bairros
class Neighborhood(models.Model):
    neighborhood = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Nome do Bairro')
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data de Criação')
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Data de Atualização')

    class Meta:
        ordering = ['neighborhood']
        verbose_name = 'Nome do Bairro'
        verbose_name_plural = 'Nomes dos Bairros'

    def __str__(self):
        return self.neighborhood

    def clean(self):
        self.neighborhood = self.neighborhood.upper()

        if Neighborhood.objects.filter(neighborhood=self.neighborhood).exclude(pk=self.pk).exists():
            raise ValidationError({'neighborhood': 'Já existe um bairro com esse nome.'})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


# Cadastro dos Bairros
class Crass(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='crass_user',
        verbose_name='Cras')
    crassOrigin = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Nome do Cras')
    name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Nome do Responsável')
    phone = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name='Telefone')
    email = models.EmailField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Email')
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data de Criação')
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Data de Atualização')

    class Meta:
        ordering = ['crassOrigin']
        verbose_name = 'Nome do Cras'
        verbose_name_plural = 'Nomes dos Cras'

    def __str__(self):
        return self.crassOrigin

    def clean(self):
        self.crassOrigin = self.crassOrigin.upper()
        self.name = self.name.upper()

        if Crass.objects.filter(crassOrigin=self.crassOrigin).exclude(pk=self.pk).exists():
            raise ValidationError({'name': 'Já existe um Cras com esse nome.'})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
