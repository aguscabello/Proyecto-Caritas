# Generated by Django 5.0.4 on 2024-05-30 18:27

import secrets
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_filial_turno_trueque'),
    ]

    operations = [
        migrations.AddField(
            model_name='trueque',
            name='token',
            field=models.CharField(default=secrets.token_urlsafe, max_length=100, unique=True),
        ),
    ]