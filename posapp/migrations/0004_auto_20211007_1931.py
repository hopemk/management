# Generated by Django 3.2.8 on 2021-10-07 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posapp', '0003_auto_20211007_1910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='quantity_after_sale',
        ),
        migrations.RemoveField(
            model_name='product',
            name='quantity_before_sale',
        ),
    ]
