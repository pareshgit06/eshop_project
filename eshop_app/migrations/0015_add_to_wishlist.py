# Generated by Django 5.1.1 on 2024-10-19 05:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_app', '0014_product_quantity_add_to_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_to_Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media')),
                ('original_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('product_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='eshop_app.product')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='eshop_app.user')),
            ],
        ),
    ]
