# Generated by Django 4.0.4 on 2022-05-17 06:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashbook', '0003_remove_cashbook_email_remove_cashbook_mobile_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashbook',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 5, 17, 12, 27, 25, 581196)),
        ),
    ]
