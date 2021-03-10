# Generated by Django 3.1.7 on 2021-03-10 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_chapter_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='url',
            field=models.CharField(default='/no-url/', max_length=100, verbose_name='book url'),
        ),
    ]
