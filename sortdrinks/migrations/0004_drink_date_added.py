# Generated by Django 2.1.1 on 2018-11-13 20:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sortdrinks', '0003_auto_20180927_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='drink',
            name='date_added',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2018, 10, 23, 20, 32, 50, 250099, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
