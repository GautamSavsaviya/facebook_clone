# Generated by Django 5.0.1 on 2024-01-28 06:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user_auth", "0005_alter_user_managers"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="user",
            name="is_staff",
            field=models.BooleanField(default=False),
        ),
    ]
