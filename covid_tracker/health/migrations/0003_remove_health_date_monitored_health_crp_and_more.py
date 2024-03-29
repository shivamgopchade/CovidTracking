# Generated by Django 4.0 on 2021-12-17 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0002_alter_health_date_monitored'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='health',
            name='date_monitored',
        ),
        migrations.AddField(
            model_name='health',
            name='crp',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=2),
        ),
        migrations.AlterField(
            model_name='health',
            name='bp_level',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='health',
            name='o2_level',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='health',
            name='sugar_level',
            field=models.IntegerField(),
        ),
    ]
