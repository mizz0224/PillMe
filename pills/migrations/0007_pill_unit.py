# Generated by Django 2.2.5 on 2020-09-27 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pills', '0006_auto_20200927_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='pill',
            name='unit',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
