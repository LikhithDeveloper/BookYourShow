from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_book_screen_no_slot_register_screen_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='id',
        ),
        migrations.RemoveField(
            model_name='slot_register',
            name='id',
        ),
        migrations.AlterField(
            model_name='book',
            name='screen_no',
            field=models.CharField(default='1', max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='slot_register',
            name='screen_no',
            field=models.CharField(default='1', max_length=20, unique=True),
        ),
    ]
