# Generated by Django 4.0 on 2021-12-17 16:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0007_alter_health_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='health',
            name='date',
            field=models.DateField(default=datetime.date(2021, 12, 17)),
        ),
    ]
