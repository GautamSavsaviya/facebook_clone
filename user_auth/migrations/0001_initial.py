# Generated by Django 5.0.1 on 2024-01-28 05:58

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("full_name", models.CharField(max_length=200)),
                ("username", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("phone", models.CharField(max_length=200)),
                (
                    "gender",
                    models.CharField(
                        choices=[("male", "Male"), ("female", "Female")], max_length=100
                    ),
                ),
                ("otp", models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
