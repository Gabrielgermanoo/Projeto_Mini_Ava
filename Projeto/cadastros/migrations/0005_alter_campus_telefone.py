# Generated by Django 4.0.6 on 2022-08-08 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0004_alter_comprovante_arquivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campus',
            name='telefone',
            field=models.CharField(max_length=14),
        ),
    ]
