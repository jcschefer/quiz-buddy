# Generated by Django 2.0 on 2018-08-17 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_auto_20180816_0156'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Question',
            new_name='Tossup',
        ),
        migrations.RemoveField(
            model_name='packet',
            name='packet_type',
        ),
    ]
