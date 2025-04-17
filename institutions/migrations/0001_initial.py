# Generated by Django 5.0 on 2025-04-17 01:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("useful", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="TypesInstitution",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        max_length=100, unique=True, verbose_name="Tipo de Instituição"
                    ),
                ),
                (
                    "observation",
                    models.TextField(
                        blank=True, max_length=255, null=True, verbose_name="Observação"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Data de Criação"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Data de Atualização"
                    ),
                ),
            ],
            options={
                "verbose_name": "Tipo de Instituição",
                "verbose_name_plural": "Tipos de Instituições",
                "ordering": ["type"],
            },
        ),
        migrations.CreateModel(
            name="Institution",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=100, verbose_name="Nome da Instituição"
                    ),
                ),
                (
                    "cnpj",
                    models.CharField(
                        blank=True,
                        max_length=15,
                        null=True,
                        unique=True,
                        verbose_name="CNPJ",
                    ),
                ),
                (
                    "address",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Endereço da Instituição",
                    ),
                ),
                (
                    "number",
                    models.CharField(
                        blank=True, max_length=10, null=True, verbose_name="Número"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=255, unique=True, verbose_name="Email"
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        blank=True, max_length=15, null=True, verbose_name="Telefone"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Data de Criação"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Data de Atualização"
                    ),
                ),
                (
                    "neighborhood",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="useful.neighborhood",
                        verbose_name="Bairro",
                    ),
                ),
                (
                    "typesInstitution",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="typesInstitution",
                        to="institutions.typesinstitution",
                        verbose_name="Tipo de Instituição",
                    ),
                ),
            ],
            options={
                "verbose_name": "Instituição",
                "verbose_name_plural": "Instituições",
                "ordering": ["name"],
            },
        ),
    ]
