# Generated by Django 2.2.5 on 2020-09-16 10:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pills', '0002_auto_20200910_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pill',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pills', to=settings.AUTH_USER_MODEL),
        ),
    ]
