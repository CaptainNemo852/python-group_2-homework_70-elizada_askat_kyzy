# Generated by Django 2.1.7 on 2019-03-02 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20190302_1206'),
    ]

    operations = [
        migrations.RenameField(
            model_name='show',
            old_name='end',
            new_name='end_time',
        ),
        migrations.RenameField(
            model_name='show',
            old_name='start',
            new_name='start_time',
        ),
    ]