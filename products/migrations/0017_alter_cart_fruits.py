# Generated by Django 4.1.4 on 2022-12-21 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_alter_cart_fruits'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='fruits',
            field=models.ManyToManyField(blank=True, to='products.product'),
        ),
    ]