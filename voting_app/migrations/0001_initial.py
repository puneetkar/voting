# Generated by Django 5.1.5 on 2025-02-06 14:25

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Vote",
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
                ("choice", models.CharField(max_length=10)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
