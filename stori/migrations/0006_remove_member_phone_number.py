# Generated by Django 2.0.3 on 2018-04-13 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stori', '0005_auto_20180413_0058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='phone_number',
        ),
    ]