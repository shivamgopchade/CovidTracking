# Generated by Django 4.0 on 2021-12-17 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0011_alter_health_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='health',
            name='date',
        ),
    ]
