# Generated by Django 3.2.9 on 2022-05-08 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.TextField(blank=True, default='sample.jpeg'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='mobile_no',
            field=models.TextField(blank=True),
        ),
    ]
