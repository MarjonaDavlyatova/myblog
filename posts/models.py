from pydoc import describe
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils import timezone


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=500)
    # created_date = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"Post {self.title}"
    