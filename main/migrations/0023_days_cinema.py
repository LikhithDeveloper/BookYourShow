# Generated by Django 5.0.6 on 2024-05-31 09:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_timeings_alter_days_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='days',
            name='cinema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Book'),
            preserve_default=False,
        ),
    ]
