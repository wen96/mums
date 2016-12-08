# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-12-08 09:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('product_type', models.CharField(choices=[(b'piece', b'Calculate price by piece'), (b'weight', b'Calcula price by weight')], max_length=6)),
                ('price', models.DecimalField(decimal_places=2, max_digits=19)),
            ],
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mumsapi.Product')),
            ],
        ),
        migrations.AddField(
            model_name='menu',
            name='products',
            field=models.ManyToManyField(related_name='menus', to='mumsapi.Product'),
        ),
    ]