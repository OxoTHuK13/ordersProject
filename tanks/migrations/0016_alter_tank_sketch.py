# Generated by Django 4.1.5 on 2023-01-10 21:36

from django.db import migrations, models
import tanks.models


class Migration(migrations.Migration):

    dependencies = [
        ('tanks', '0015_tank_sketch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tank',
            name='sketch',
            field=models.ImageField(blank=True, null=True, upload_to=tanks.models.get_path_for_sketches, verbose_name='Чертеж'),
        ),
    ]
