# Generated by Django 4.1 on 2022-12-03 14:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_transaction_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='data',
        ),
        migrations.AddField(
            model_name='transaction',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 12, 3, 19, 5, 38, 71425)),
        ),
    ]
