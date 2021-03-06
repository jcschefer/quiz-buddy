# Generated by Django 2.0 on 2017-12-31 03:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Packet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('index', models.IntegerField(help_text='Order that the packet comes in the tournament')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1500)),
                ('answer', models.CharField(max_length=250)),
                ('packet_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Packet')),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='packet',
            name='tournament_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Tournament'),
        ),
    ]
