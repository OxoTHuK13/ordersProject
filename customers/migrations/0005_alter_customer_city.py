# Generated by Django 4.1.5 on 2023-01-06 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_region_city_customer_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='city',
            field=models.ManyToManyField(to='customers.city', verbose_name='Город'),
        ),
    ]