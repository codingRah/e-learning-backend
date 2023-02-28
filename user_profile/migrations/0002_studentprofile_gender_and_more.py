# Generated by Django 4.1.7 on 2023-02-28 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Others')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='first_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='last_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
