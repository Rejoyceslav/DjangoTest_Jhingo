# Generated by Django 3.2.6 on 2021-09-07 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0010_auto_20210907_2057'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='group',
            new_name='group_selected',
        ),
    ]
