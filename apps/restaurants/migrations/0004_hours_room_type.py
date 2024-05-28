# Generated by Django 5.0 on 2024-04-27 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hours',
            name='room_type',
            field=models.CharField(choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner')], default=1, max_length=20),
            preserve_default=False,
        ),
    ]
