# Generated by Django 2.2.5 on 2020-09-16 13:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pills', '0003_auto_20200916_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pill',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pills', to=settings.AUTH_USER_MODEL),
        ),
    ]