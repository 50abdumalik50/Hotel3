from django.db import models
from django.contrib.auth import get_user_model

from apps.rooms.models import Room

User = get_user_model()


class Comment(models.Model):
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    text = models.CharField(
        max_length=500,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.user} - {self.text}"

