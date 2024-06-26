# Generated by Django 5.0.3 on 2024-04-02 16:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('phone_number', models.PositiveIntegerField(blank=True, null=True)),
                ('adress', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.adress')),
            ],
        ),
    ]
