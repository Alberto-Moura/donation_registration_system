from django.db import models
from django.core.exceptions import ValidationError


# Cadastro das categorias
class Category(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Nome da Categoria')
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
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name

    def clean(self):
        self.name = self.name.upper()
        self.observation = self.observation.upper()

        if Category.objects.filter(name=self.name).exclude(pk=self.pk).exists():
            raise ValidationError({'name': 'Já existe uma categoria com esse nome.'})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class Acronym(models.Model):
    acronym = models.CharField(
        max_length=4,
        unique=True,
        verbose_name='Sigla')
    description = models.CharField(
        max_length=100,
        verbose_name='Descrição')
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data de Criação')
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Data de Atualização')

    class Meta:
        ordering = ['acronym']
        verbose_name = 'Sigla'
        verbose_name_plural = 'Siglas'

    def __str__(self):
        return self.acronym

    def clean(self):
        self.acronym = self.acronym.upper()
        self.description = self.description.upper()

        if Acronym.objects.filter(acronym=self.acronym).exclude(pk=self.pk).exists():
            raise ValidationError({'acronym': 'Já existe uma sigla com esse nome.'})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


# Cadastro dos produtos
class Product(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Nome do Produto')
    unit_quantity = models.PositiveIntegerField(
        verbose_name='Quantidade Unitária')
    compound_quantity = models.PositiveIntegerField(
        default=1,
        verbose_name='Quantidade composta')
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='category',
        verbose_name='Categoria do Produto')
    acronym = models.ForeignKey(
        Acronym,
        on_delete=models.PROTECT,
        verbose_name='Sigla')
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
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.name

    def clean(self):
        self.name = self.name.upper()
        self.observation = self.observation.upper()

        if Category.objects.filter(name=self.name).exclude(pk=self.pk).exists():
            raise ValidationError({'name': 'Já existe um produto com esse nome.'})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
