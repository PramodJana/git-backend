# Generated by Django 2.1.2 on 2018-10-21 20:01

from decimal import Decimal
import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house_renting_app', '0003_auto_20181021_1827'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hostels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', django.contrib.gis.db.models.fields.PointField(null=True, srid=4326)),
                ('address', models.CharField(max_length=100, null=True)),
                ('hostel_room_size', models.IntegerField(null=True)),
                ('hostel_floor_no', models.IntegerField(null=True)),
                ('hostel_room_type', models.BooleanField(default=True)),
                ('hostel_attached_bathroom', models.BooleanField(default=True)),
                ('hostel_mess_facility', models.BooleanField(default=True)),
                ('hostel_other_facilities1', models.BooleanField(default=True)),
                ('hostel_other_facilities2', models.BooleanField(default=True)),
                ('hostel_other_facilities3', models.BooleanField(default=True)),
                ('hostel_other_facilities4', models.BooleanField(default=True)),
                ('hostel_price', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)),
                ('apartment_description', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'Hostels',
            },
        ),
        migrations.CreateModel(
            name='Houses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', django.contrib.gis.db.models.fields.PointField(null=True, srid=4326)),
                ('address', models.CharField(max_length=100, null=True)),
                ('house_no_bedrooms', models.IntegerField(null=True)),
                ('house_no_bathrooms', models.IntegerField(null=True)),
                ('house_tenants_preffered', models.CharField(max_length=10)),
                ('house_carpet_area', models.IntegerField(null=True)),
                ('house_buildup_area', models.IntegerField(null=True)),
                ('house_furnishing', models.CharField(max_length=15)),
                ('house_overlooking', models.CharField(max_length=30)),
                ('house_floor_no', models.IntegerField(null=True)),
                ('house_price', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)),
                ('house_description', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Houses',
            },
        ),
    ]
