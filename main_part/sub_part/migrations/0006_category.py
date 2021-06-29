# Generated by Django 3.2.3 on 2021-06-11 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0005_adminuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Enter_Price', models.CharField(max_length=100)),
                ('Parent_Category', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/%Y/%m/%d')),
            ],
        ),
    ]
