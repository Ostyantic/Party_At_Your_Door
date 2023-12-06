from django.db import models
from django.contrib.auth import get_user_model


class Singer(models.Model):
    name = models.CharField(max_length=20)
    song_name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

