# Generated by Django 3.2.8 on 2021-10-07 19:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sell', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sell',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
