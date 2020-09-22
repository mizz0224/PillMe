# Generated by Django 2.2.5 on 2020-09-21 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pills', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pill',
            name='major_axis',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='pill',
            name='minor_axis',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='pill',
            name='thickness',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
