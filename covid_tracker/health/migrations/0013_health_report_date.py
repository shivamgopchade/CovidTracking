# Generated by Django 4.0 on 2021-12-17 17:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0012_remove_health_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='health',
            name='report_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
