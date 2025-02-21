# Generated by Django 5.1.6 on 2025-02-21 12:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('created_ed', models.DateTimeField(auto_now_add=True)),
                ('updated_ed', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='cars')),
                ('color', models.TextField(blank=True)),
                ('ot_kuchi', models.TextField(blank=True)),
                ('year', models.TextField(blank=True)),
                ('price', models.TextField(blank=True)),
                ('context', models.TextField(blank=True)),
                ('created_ed', models.DateTimeField(auto_now_add=True)),
                ('updated_ed', models.DateTimeField(auto_now=True)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('is_bool', models.BooleanField(default=True)),
                ('carmodel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configapp.carmodel')),
            ],
            options={
                'verbose_name': 'Cars',
                'verbose_name_plural': 'Cars',
                'ordering': ['created_ed'],
            },
        ),
    ]
