# Generated by Django 3.1 on 2020-08-15 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0006_comments'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
    ]
