# Generated by Django 3.2.3 on 2021-06-12 02:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0016_course'),
    ]

    operations = [
        migrations.RenameField(
            model_name='allstudents',
            old_name='first_name',
            new_name='First_name',
        ),
    ]
