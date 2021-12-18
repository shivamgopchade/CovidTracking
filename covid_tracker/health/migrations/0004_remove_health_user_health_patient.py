# Generated by Django 4.0 on 2021-12-17 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('health', '0003_remove_health_date_monitored_health_crp_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='health',
            name='user',
        ),
        migrations.AddField(
            model_name='health',
            name='patient',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]