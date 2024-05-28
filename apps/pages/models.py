import os
from django.db import models

from utils.image_path import upload_teams


class Service(models.Model):
    name = models.CharField(
        max_length=50
    )
    description = models.TextField(
        max_length=100
    )


class Team(models.Model):
    name = models.CharField(
        max_length=50,
    )
    occupation = models.CharField(
        max_length=50,
    )


class TeamImage(models.Model):
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE,
        related_name='images',
    )
    image = models.ImageField(
        upload_to=upload_teams,
    )

    def delete(self, using=None, keep_parents=False):
        os.remove(self.image.path)
        super().delete(using=None, keep_parents=False)

    def __str__(self):
        return f"{self.image.url}"