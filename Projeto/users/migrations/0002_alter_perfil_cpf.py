# Generated by Django 4.0.6 on 2022-08-08 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='cpf',
            field=models.CharField(max_length=14, null=True, unique=True, verbose_name='CPF'),
        ),
    ]
