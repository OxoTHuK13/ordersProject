# Generated by Django 4.1.5 on 2023-01-08 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tanks', '0008_cost_dut_tank_difficult_koef'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tank',
            name='difficult_koef',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=6, null=True, verbose_name='Надбавка за сложность, руб'),
        ),
    ]
