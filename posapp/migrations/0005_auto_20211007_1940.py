# Generated by Django 3.2.8 on 2021-10-07 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posapp', '0004_auto_20211007_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity_after_sale',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='quantity_before_sale',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
