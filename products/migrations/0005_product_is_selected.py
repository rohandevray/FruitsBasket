# Generated by Django 4.1.4 on 2022-12-17 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_rename_name_product_fruit_name_product_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_selected',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
