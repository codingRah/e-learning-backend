# Generated by Django 4.1.5 on 2023-01-28 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('code', models.CharField(blank=True, max_length=50, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=255, unique=True)),
                ('details', models.CharField(blank=True, max_length=255, null=True)),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='user_profile.province')),
            ],
        ),
    ]
