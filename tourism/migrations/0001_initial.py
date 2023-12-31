# Generated by Django 4.2.4 on 2023-09-10 16:11

from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('agency_name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('last_price', models.IntegerField()),
                ('staying_time', models.CharField(max_length=200)),
                ('trip_type', models.CharField(max_length=200)),
                ('start_date', django_jalali.db.models.jDateField()),
                ('end_date', django_jalali.db.models.jDateField()),
                ('start_point', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('agency_services', models.CharField(max_length=300)),
                ('destination_description', models.TextField(default='', max_length=1000)),
                ('additional_description', models.TextField(default='', max_length=1000)),
                ('agency', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='tourism.agency')),
            ],
        ),
    ]
