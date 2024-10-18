# Generated by Django 5.1.2 on 2024-10-18 09:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='APIInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Api Name')),
                ('api_key', models.CharField(max_length=256, verbose_name='Api Key')),
                ('detail', models.TextField(verbose_name='Api Detail')),
                ('client_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='Client Id')),
                ('client_secret', models.CharField(blank=True, max_length=255, null=True, verbose_name='Client Secret')),
                ('doc_url', models.CharField(max_length=256, verbose_name='Api Doc Url')),
                ('spare_1', models.CharField(blank=True, max_length=255, null=True, verbose_name='Spare 1')),
                ('spare_2', models.CharField(blank=True, max_length=255, null=True, verbose_name='Spare 2')),
                ('spare_3', models.CharField(blank=True, max_length=255, null=True, verbose_name='Spare 3')),
                ('spare_4', models.CharField(blank=True, max_length=255, null=True, verbose_name='Spare 4')),
            ],
        ),
        migrations.CreateModel(
            name='FinanceCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=256, verbose_name='Finans Category')),
            ],
        ),
        migrations.CreateModel(
            name='SponsorInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('widget_number', models.PositiveIntegerField(verbose_name='Widget Number')),
                ('name', models.CharField(max_length=256, verbose_name='Sponsor Name')),
                ('number', models.CharField(max_length=2, verbose_name='Sponsor Lct')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active?')),
                ('code', models.TextField(verbose_name='Iframe Code')),
            ],
        ),
        migrations.CreateModel(
            name='Alarm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('widget_number', models.PositiveIntegerField(verbose_name='Widget Number')),
                ('name', models.CharField(max_length=256, verbose_name='Alarm Name')),
                ('additional_info', models.CharField(choices=[('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly')], max_length=50, verbose_name='Additional Info')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active?')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Finance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('widget_number', models.PositiveIntegerField(verbose_name='Widget Number')),
                ('name', models.CharField(max_length=256, verbose_name='Alarm Name')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
                ('categories', models.ManyToManyField(to='api.financecategory', verbose_name='Finance Category')),
            ],
        ),
        migrations.CreateModel(
            name='GetUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('widget_number', models.PositiveIntegerField(verbose_name='Widget Number')),
                ('exercise', models.PositiveIntegerField(verbose_name='Exercise Point')),
                ('reminder', models.PositiveIntegerField(verbose_name='Reminder Point')),
                ('date', models.DateField(verbose_name='Date')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('widget_number', models.PositiveIntegerField(verbose_name='Widget Number')),
                ('image', models.FileField(max_length=255, upload_to='images/', verbose_name='İmage')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('widget_number', models.PositiveIntegerField(verbose_name='Widget Number')),
                ('country', models.CharField(max_length=100, verbose_name='Country')),
                ('language', models.CharField(max_length=50, verbose_name='Language')),
                ('category', models.CharField(choices=[('General', 'General'), ('Business', 'Business'), ('Entertainment', 'Entertainment'), ('Health', 'Health'), ('Technology', 'Technology')], max_length=256, verbose_name='Category')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('widget_number', models.PositiveIntegerField(verbose_name='Widget Number')),
                ('note', models.CharField(max_length=500, verbose_name='Note')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Quotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('widget_number', models.PositiveIntegerField(verbose_name='Widget Number')),
                ('text', models.CharField(max_length=256, verbose_name='Quotes Text')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Shortcut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('widget_number', models.PositiveIntegerField(verbose_name='Widget Number')),
                ('name', models.CharField(max_length=256, verbose_name='Shortcut Name')),
                ('url', models.CharField(max_length=256, verbose_name='Shortcut Url')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('widget_number', models.PositiveIntegerField(verbose_name='Widget Number')),
                ('name', models.CharField(max_length=256, verbose_name='Todo Name')),
                ('is_complete', models.BooleanField(verbose_name='Complete?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='UserIp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('register_ip', models.CharField(max_length=50, verbose_name='Register IP')),
                ('mail_verified', models.BooleanField(default=False, verbose_name='Verified?')),
                ('mail_verified_at', models.DateField(blank=True, null=True, verbose_name='Mail Verified At')),
                ('change_pass_at', models.DateField(blank=True, null=True, verbose_name='Password Verified At')),
                ('is_delete', models.BooleanField(default=False, verbose_name='Delete?')),
                ('country', models.CharField(max_length=100, verbose_name='Country')),
                ('city', models.CharField(max_length=256, verbose_name='City')),
                ('language', models.CharField(max_length=50, verbose_name='Language')),
                ('last_send_mail', models.DateField(blank=True, null=True, verbose_name='Send Mail At')),
                ('user', models.OneToOneField(default='Silindi', on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
