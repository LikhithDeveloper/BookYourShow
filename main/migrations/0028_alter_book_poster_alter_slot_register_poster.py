# Generated by Django 5.0.6 on 2024-05-31 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_alter_book_poster_alter_slot_register_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='poster',
            field=models.ImageField(default=False, upload_to='posters'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='slot_register',
            name='poster',
            field=models.ImageField(default=False, upload_to='posters'),
            preserve_default=False,
        ),
    ]
