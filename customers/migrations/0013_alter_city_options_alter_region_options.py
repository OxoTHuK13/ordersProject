# Generated by Django 4.1.5 on 2023-01-10 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0012_customer_email_alter_customer_passport'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['region', 'name'], 'verbose_name': 'Город', 'verbose_name_plural': 'Города'},
        ),
        migrations.AlterModelOptions(
            name='region',
            options={'ordering': ['name'], 'verbose_name': 'Регион', 'verbose_name_plural': 'Регионы'},
        ),
    ]
