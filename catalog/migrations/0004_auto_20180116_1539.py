# Generated by Django 2.0.1 on 2018-01-16 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20180116_1536'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='autho',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='titl',
            new_name='title',
        ),
    ]
