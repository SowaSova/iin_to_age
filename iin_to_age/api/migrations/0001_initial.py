# Generated by Django 3.2.14 on 2022-08-31 13:52

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Person",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "iin",
                    models.CharField(
                        max_length=12,
                        unique=True,
                        validators=[api.models.validate_length],
                        verbose_name="IIN",
                    ),
                ),
            ],
        ),
    ]
