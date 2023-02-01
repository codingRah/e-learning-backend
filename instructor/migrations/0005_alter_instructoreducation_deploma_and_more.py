# Generated by Django 4.1.5 on 2023-01-31 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("instructor", "0004_alter_instructoreducation_instructor_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="instructoreducation",
            name="deploma",
            field=models.ImageField(upload_to="instructor_education/deploma"),
        ),
        migrations.AlterField(
            model_name="instructoridcart",
            name="id_back",
            field=models.ImageField(upload_to="instructor-id/back"),
        ),
        migrations.AlterField(
            model_name="instructoridcart",
            name="id_front",
            field=models.ImageField(upload_to="instructor-id/front"),
        ),
        migrations.AlterField(
            model_name="instructoridcart",
            name="passport_back",
            field=models.ImageField(upload_to="instructor-passport/back"),
        ),
        migrations.AlterField(
            model_name="instructoridcart",
            name="passport_front",
            field=models.ImageField(upload_to="instructor-passport/frant"),
        ),
    ]
