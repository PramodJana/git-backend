# Generated by Django 2.0.9 on 2018-11-29 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('house_renting_app', '0020_auto_20181128_1137'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hostels',
            old_name='images4',
            new_name='images1',
        ),
        migrations.RenameField(
            model_name='hostels',
            old_name='images5',
            new_name='images2',
        ),
        migrations.RenameField(
            model_name='hostels',
            old_name='images6',
            new_name='images3',
        ),
        migrations.RenameField(
            model_name='houses',
            old_name='images7',
            new_name='images1',
        ),
        migrations.RenameField(
            model_name='houses',
            old_name='images8',
            new_name='images2',
        ),
        migrations.RenameField(
            model_name='houses',
            old_name='images9',
            new_name='images3',
        ),
    ]
