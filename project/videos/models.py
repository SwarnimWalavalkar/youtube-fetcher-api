import uuid
from django.db import models


class Video(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False),
    title = models.CharField(max_length=100)
    description = models.TextField()
    published_on = models.DateTimeField()
    thumbnail_url = models.CharField(max_length=100)
    video_url = models.CharField(max_length=100)

    class Meta:
        indexes = [
            models.Index(fields=["title", "description"])
        ]
