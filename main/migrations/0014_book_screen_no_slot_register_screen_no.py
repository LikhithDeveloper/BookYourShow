# Generated by Django 5.0.6 on 2024-05-29 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_book_description_slot_register_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='screen_no',
            field=models.CharField(default='1', max_length=20),
        ),
        migrations.AddField(
            model_name='slot_register',
            name='screen_no',
            field=models.CharField(default='1', max_length=20),
        ),
    ]
