# Generated by Django 3.0.8 on 2020-07-17 16:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_data',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 17, 16, 50, 28, 27426, tzinfo=utc)),
        ),
    ]
