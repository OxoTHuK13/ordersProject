# Generated by Django 4.1.5 on 2023-02-06 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tanks', '0020_remove_tanktovehiclemodel_vehicle'),
    ]

    operations = [
        migrations.AddField(
            model_name='tanktovehiclemodel',
            name='vehicle',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='tanks.vehicle', verbose_name='ТС'),
            preserve_default=False,
        ),
    ]
