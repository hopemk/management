# Generated by Django 3.2.8 on 2021-11-25 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0003_auto_20211125_0718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkinout',
            name='check_in',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='checkinout',
            name='check_out',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='checkinout',
            name='checkout_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
