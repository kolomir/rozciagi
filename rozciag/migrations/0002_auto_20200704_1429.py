# Generated by Django 3.0.8 on 2020-07-04 12:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rozciag', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rozciagi',
            name='lista',
        ),
        migrations.AlterField(
            model_name='rozciagi',
            name='data_dodania',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 4, 14, 29, 24, 720552), verbose_name='data dodania'),
        ),
        migrations.DeleteModel(
            name='Lista',
        ),
    ]
