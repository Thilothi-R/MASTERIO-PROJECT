# Generated by Django 3.2.3 on 2021-06-11 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0003_allstudents'),
    ]

    operations = [
        migrations.RenameField(
            model_name='allstudents',
            old_name='First_name',
            new_name='first_name',
        ),
    ]
