# Generated by Django 5.0 on 2025-04-23 00:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("donation_entry", "0003_donateditem_observation"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="donateditem",
            options={"ordering": ["id"], "verbose_name": "Relatório de Entrada"},
        ),
    ]
