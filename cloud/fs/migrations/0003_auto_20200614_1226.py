# Generated by Django 3.0.7 on 2020-06-14 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fs', '0002_auto_20200614_1223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gateway',
            name='gateway_name',
        ),
        migrations.RemoveField(
            model_name='project',
            name='queue_name',
        ),
    ]