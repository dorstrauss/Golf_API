# Generated by Django 4.1.3 on 2022-12-05 08:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='registration_date',
            field=models.DateTimeField(default=datetime.date(2022, 12, 5)),
        ),
    ]
