# Generated by Django 2.1.2 on 2018-11-26 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('house_renting_app', '0014_auto_20181126_1541'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apartment',
            old_name='apartmrnt_owner_mail',
            new_name='apartment_owner_mail',
        ),
    ]
