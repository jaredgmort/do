# Generated by Django 2.0.3 on 2018-04-03 16:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stori', '0002_auto_20180403_1319'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='name',
            new_name='full_name',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='number',
            new_name='phone_number',
        ),
        migrations.AddField(
            model_name='member',
            name='date_birth',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='gender',
            field=models.CharField(default=datetime.date(2018, 4, 3), max_length=250),
            preserve_default=False,
        ),
    ]
