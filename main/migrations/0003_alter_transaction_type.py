# Generated by Django 4.1 on 2022-11-13 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_category_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='type',
            field=models.BooleanField(verbose_name='Доход'),
        ),
    ]