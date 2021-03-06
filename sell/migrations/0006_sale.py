# Generated by Django 3.2.8 on 2021-10-12 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posapp', '0007_remove_product_quantity_after_sale'),
        ('sell', '0005_alter_sell_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items_sold', models.IntegerField()),
                ('paid', models.FloatField(max_length=280)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('peoduct', models.ManyToManyField(to='posapp.Product')),
            ],
        ),
    ]
