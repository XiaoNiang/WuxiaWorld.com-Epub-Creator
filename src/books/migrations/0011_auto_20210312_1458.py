# Generated by Django 3.1.7 on 2021-03-12 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_auto_20210312_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='url',
            field=models.CharField(default='/no-url/', max_length=100, verbose_name='book url'),
        ),
    ]
