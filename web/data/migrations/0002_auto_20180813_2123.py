# Generated by Django 2.0 on 2018-08-13 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    atomic = False

    operations = [
        migrations.RenameModel(
            old_name='Packet',
            new_name='Round',
        ),
        migrations.RemoveField(
            model_name='question',
            name='text',
        ),
        migrations.AddField(
            model_name='question',
            name='text_part_1',
            field=models.CharField(default='default question text', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='text_part_2',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='question',
            name='text_part_3',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
