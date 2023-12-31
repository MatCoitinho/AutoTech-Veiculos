# Generated by Django 4.2.4 on 2023-09-12 02:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('cpf', models.CharField(max_length=14, unique=True, verbose_name='CPF')),
                ('senha', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='O número de telefone deve ter 10 dígitos (apenas números).', regex='^\\d{10}$')], verbose_name='Telefone')),
                ('endereco', models.CharField(max_length=300)),
                ('admin', models.BooleanField(verbose_name='Permissao Admin')),
            ],
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
    ]
