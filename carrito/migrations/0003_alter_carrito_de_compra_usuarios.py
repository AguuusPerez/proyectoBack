# Generated by Django 5.0.6 on 2024-06-13 00:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrito', '0002_initial'),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrito_de_compra',
            name='usuarios',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='usuarios.customuser'),
        ),
    ]
