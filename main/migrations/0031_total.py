# Generated by Django 5.0.6 on 2024-06-01 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_bookedseat_total_seats'),
    ]

    operations = [
        migrations.CreateModel(
            name='Total',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_no', models.IntegerField()),
            ],
        ),
    ]
