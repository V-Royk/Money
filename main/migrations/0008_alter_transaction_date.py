# Generated by Django 4.1 on 2022-12-03 14:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_transaction_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 12, 3, 19, 33, 59, 163435)),
        ),
    ]
