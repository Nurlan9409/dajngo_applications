# Generated by Django 5.0.3 on 2024-04-02 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_comment_student_alter_comment_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='book',
        ),
        migrations.AddField(
            model_name='book',
            name='coments',
            field=models.ManyToManyField(to='library.comment'),
        ),
    ]
