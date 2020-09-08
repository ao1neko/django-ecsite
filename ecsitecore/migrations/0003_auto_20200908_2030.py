# Generated by Django 3.0.7 on 2020-09-08 11:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecsitecore', '0002_auto_20200908_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='num',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1)], verbose_name='数量'),
        ),
    ]