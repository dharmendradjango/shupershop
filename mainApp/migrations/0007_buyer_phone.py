# Generated by Django 5.0.3 on 2024-03-27 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0006_alter_buyer_pin'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='phone',
            field=models.CharField(default='', max_length=15),
        ),
    ]
