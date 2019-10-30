# Generated by Django 2.2.6 on 2019-10-29 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('errors', '0003_remove_error_excluded'),
    ]

    operations = [
        migrations.AlterField(
            model_name='error',
            name='level',
            field=models.CharField(choices=[('debug', 'Debug'), ('error', 'Error'), ('warning', 'Warning')], max_length=20, verbose_name='Tipo'),
        ),
    ]