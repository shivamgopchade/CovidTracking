# Generated by Django 4.0 on 2021-12-18 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_profile_age_profile_smoker_drinker'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='smoker_drinker',
            new_name='tippler',
        ),
    ]
