# Generated by Django 5.0.2 on 2024-02-26 08:54

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Apple",
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
                ("name", models.CharField(max_length=100)),
                ("amount", models.CharField(max_length=100)),
                ("paymentid", models.CharField(max_length=100)),
                ("paid", models.BooleanField(default=False)),
            ],
        ),
    ]
