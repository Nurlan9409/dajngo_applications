# Generated by Django 5.0.3 on 2024-04-02 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_remove_book_coments_bookingbook_coments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookingbook',
            name='coments',
        ),
        migrations.AddField(
            model_name='book',
            name='coments',
            field=models.ManyToManyField(to='library.comment'),
        ),
    ]
