from django.db import models
from django.utils.timezone import now

class Post(models.Model):
    username = models.TextField()
    created_datetime = models.DateTimeField(default=now)
    title = models.TextField()
    content = models.TextField()