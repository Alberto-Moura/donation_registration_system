# Generated by Django 5.0 on 2025-04-21 18:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("institutions", "0006_alter_institution_neighborhood"),
        ("useful", "0002_alter_crass_options_alter_crass_crassorigin_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="donation_entry",
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
                ("date_of_contact", models.DateField(verbose_name="Data de Contato")),
                (
                    "withdrawal_date",
                    models.DateField(
                        blank=True, null=True, verbose_name="Data de Retirada"
                    ),
                ),
                (
                    "pick_up_time",
                    models.TimeField(
                        blank=True, null=True, verbose_name="Hora de Retirada"
                    ),
                ),
                (
                    "address",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="Endereço"
                    ),
                ),
                (
                    "number",
                    models.CharField(
                        blank=True, max_length=10, null=True, verbose_name="Número"
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        blank=True, max_length=15, null=True, verbose_name="Telefone"
                    ),
                ),
                (
                    "contact",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Contato"
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
                (
                    "name",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="institution",
                        to="institutions.institution",
                        verbose_name="Nome do Doador",
                    ),
                ),
                (
                    "neighborhood",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="useful.neighborhood",
                        verbose_name="Bairro",
                    ),
                ),
                (
                    "typesInstitution",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="typesinstitution",
                        to="institutions.typesinstitution",
                        verbose_name="Tipo de Doador",
                    ),
                ),
            ],
            options={
                "verbose_name": "Cadastrar Entrada",
                "verbose_name_plural": "Cadastrar Entradas",
                "ordering": ["id"],
            },
        ),
    ]
