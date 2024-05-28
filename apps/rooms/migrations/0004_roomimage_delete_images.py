# Generated by Django 5.0 on 2024-04-28 06:28

import django.db.models.deletion
import utils.image_path
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0003_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=utils.image_path.upload_rooms)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='rooms.room')),
            ],
        ),
        migrations.DeleteModel(
            name='Images',
        ),
    ]