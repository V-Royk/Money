# Generated by Django 4.1 on 2022-12-03 13:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_category_id_transaction_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='data',
            field=models.DateField(default=datetime.datetime(2022, 12, 3, 18, 52, 5, 778239)),
        ),
    ]