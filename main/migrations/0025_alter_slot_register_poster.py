# Generated by Django 5.0.6 on 2024-05-31 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_alter_slot_register_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot_register',
            name='poster',
            field=models.ImageField(upload_to='poster'),
        ),
    ]
