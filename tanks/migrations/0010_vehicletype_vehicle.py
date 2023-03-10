# Generated by Django 4.1.5 on 2023-01-09 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tanks', '0009_alter_tank_difficult_koef'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Тип ТС')),
            ],
            options={
                'verbose_name': 'Тип ТС',
                'verbose_name_plural': 'Типы ТС',
            },
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Наименование')),
                ('tank', models.ManyToManyField(to='tanks.tank', verbose_name='Наименование бака')),
                ('vehicle_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tanks.vehicletype', verbose_name='Тип ТС')),
            ],
            options={
                'verbose_name': 'Транспортное средство',
                'verbose_name_plural': 'Транспортные средства',
            },
        ),
    ]
