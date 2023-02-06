# Generated by Django 4.1.5 on 2023-02-06 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("instructor", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="instructor",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("pending", "pending"),
                    ("active", "active"),
                    ("deactive", "deactive"),
                ],
                max_length=50,
                null=True,
            ),
        ),
    ]
