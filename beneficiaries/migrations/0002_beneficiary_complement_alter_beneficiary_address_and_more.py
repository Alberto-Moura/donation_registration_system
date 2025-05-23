# Generated by Django 5.0 on 2025-04-23 02:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("beneficiaries", "0001_initial"),
        ("useful", "0003_alter_crass_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="beneficiary",
            name="complement",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Complemento"
            ),
        ),
        migrations.AlterField(
            model_name="beneficiary",
            name="address",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Endereço"
            ),
        ),
        migrations.AlterField(
            model_name="beneficiary",
            name="crassOrigin",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="crass_origin",
                to="useful.crass",
                verbose_name="CRAS de Origem",
            ),
        ),
    ]
