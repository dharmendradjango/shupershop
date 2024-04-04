# Generated by Django 5.0.3 on 2024-03-23 18:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('pic', models.ImageField(upload_to='uploads/brand')),
            ],
        ),
        migrations.CreateModel(
            name='Maincategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('baseprice', models.IntegerField()),
                ('discound', models.IntegerField()),
                ('finalprice', models.IntegerField()),
                ('stock', models.BooleanField(default=True)),
                ('color', models.CharField(max_length=30)),
                ('size', models.CharField(max_length=10)),
                ('description', models.TextField(default='')),
                ('pic1', models.ImageField(upload_to='uploads/product')),
                ('pic2', models.ImageField(blank=True, default=None, null=True, upload_to='uploads/product')),
                ('pic3', models.ImageField(blank=True, default=None, null=True, upload_to='uploads/product')),
                ('pic4', models.ImageField(blank=True, default=None, null=True, upload_to='uploads/product')),
                ('Maincategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.maincategory')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.brand')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.subcategory')),
            ],
        ),
    ]
