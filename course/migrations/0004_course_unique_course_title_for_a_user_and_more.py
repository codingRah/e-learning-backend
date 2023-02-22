# Generated by Django 4.1.5 on 2023-02-22 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_course_files'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='course',
            constraint=models.UniqueConstraint(fields=('title', 'created_by'), name='unique_course_title_for_a_user'),
        ),
        migrations.AlterModelTable(
            name='course',
            table='course_course',
        ),
    ]
