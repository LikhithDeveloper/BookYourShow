# Generated by Django 5.0.6 on 2024-05-30 16:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_remove_bookedseat_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Days',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='show',
            name='date',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.days'),
        ),
    ]