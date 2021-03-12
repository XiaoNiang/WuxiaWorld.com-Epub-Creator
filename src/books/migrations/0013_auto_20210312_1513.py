# Generated by Django 3.1.7 on 2021-03-12 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0012_auto_20210312_1500'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='url',
            new_name='siteUrl',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='sourceLink',
            new_name='sourceUrl',
        ),
        migrations.RenameField(
            model_name='chapter',
            old_name='number',
            new_name='chapterNumber',
        ),
        migrations.RenameField(
            model_name='chapter',
            old_name='text',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='chapter',
            old_name='link',
            new_name='sourceUrl',
        ),
        migrations.RenameField(
            model_name='sitemap',
            old_name='text',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='sitemap',
            old_name='url',
            new_name='sourceUrl',
        ),
    ]
