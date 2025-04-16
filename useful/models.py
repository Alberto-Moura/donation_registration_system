from django.db import models
from django.core.exceptions import ValidationError


# Cadastro dos Bairros
class Neighborhood(models.Model):
    neighborhood = models.CharField(max_length=255, unique=True, verbose_name='Nome do Bairro')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data de Atualização')

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
    crassOrigin = models.CharField(max_length=255, unique=True, verbose_name='Nome do Crass')
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Nome do Responsável')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data de Atualização')

    class Meta:
        ordering = ['crassOrigin']
        verbose_name = 'Nome do Crass'
        verbose_name_plural = 'Nomes dos Crass'

    def __str__(self):
        return self.crassOrigin

    def clean(self):
        self.crassOrigin = self.crassOrigin.upper()
        self.name = self.name.upper()

        if Crass.objects.filter(crassOrigin=self.crassOrigin).exclude(pk=self.pk).exists():
            raise ValidationError({'name': 'Já existe um Crass com esse nome.'})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
