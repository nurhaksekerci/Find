# Generated by Django 5.1.2 on 2024-10-18 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialAuthSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider', models.CharField(choices=[('google', 'Google'), ('facebook', 'Facebook')], max_length=50, unique=True)),
                ('client_id', models.CharField(max_length=255, verbose_name='Client ID')),
                ('secret_key', models.CharField(max_length=255, verbose_name='Secret Key')),
            ],
        ),
    ]