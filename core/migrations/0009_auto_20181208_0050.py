# Generated by Django 2.1.3 on 2018-12-07 19:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20181208_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateField(default=datetime.datetime(2018, 12, 7, 19, 20, 56, 706522, tzinfo=utc)),
        ),
    ]