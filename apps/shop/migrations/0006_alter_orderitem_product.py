# Generated by Django 5.1.2 on 2024-10-12 20:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_product_rating_alter_productrating_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(help_text='Product name', on_delete=django.db.models.deletion.CASCADE, related_name='items', to='shop.productsize'),
        ),
    ]
