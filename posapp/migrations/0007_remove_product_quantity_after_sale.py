# Generated by Django 3.2.8 on 2021-10-12 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posapp', '0006_rename_quantity_before_sale_product_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='quantity_after_sale',
        ),
    ]
