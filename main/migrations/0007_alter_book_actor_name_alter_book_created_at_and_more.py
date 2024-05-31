# Generated by Django 5.0.6 on 2024-05-29 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_bookedseat_id_alter_bookedseat_seat_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='actor_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='book',
            name='created_at',
            field=models.DateTimeField(default=''),
        ),
        migrations.AlterField(
            model_name='book',
            name='movie_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='book',
            name='ticket_price',
            field=models.IntegerField(default=''),
        ),
    ]
