# Generated by Django 2.0.3 on 2018-04-13 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stori', '0006_remove_member_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='phone_number',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]