# Generated by Django 3.2.8 on 2021-11-25 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0002_auto_20211125_0715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkinout',
            name='model',
        ),
        migrations.RemoveField(
            model_name='checkinout',
            name='product',
        ),
        migrations.RemoveField(
            model_name='checkinout',
            name='serial_number',
        ),
    ]
