# Generated by Django 2.0 on 2018-08-14 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_auto_20180814_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='number',
            field=models.IntegerField(default=0, help_text='Order in which the question comes in the packet'),
        ),
    ]
