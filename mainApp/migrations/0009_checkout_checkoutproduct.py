# Generated by Django 5.0.3 on 2024-03-30 11:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0008_alter_buyer_city_alter_buyer_state_wishlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('orderstatus', models.IntegerField(choices=[(0, 'Order is Placed'), (1, 'Order is Packed'), (2, 'Ready to Dispatch'), (3, 'Dispatched'), (4, 'Out For Delivery'), (5, 'Delivered')], default=0)),
                ('paymentstatus', models.IntegerField(choices=[(0, 'Pending'), (1, 'Done')], default=0)),
                ('paymentmode', models.IntegerField(choices=[(0, 'COD'), (1, 'NetBanking')], default=0)),
                ('subtotal', models.IntegerField()),
                ('shipping', models.IntegerField()),
                ('total', models.IntegerField()),
                ('rppid', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.buyer')),
            ],
        ),
        migrations.CreateModel(
            name='CheckoutProduct',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('qty', models.IntegerField()),
                ('total', models.IntegerField()),
                ('checkout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.checkout')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.product')),
            ],
        ),
    ]
