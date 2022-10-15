from pydoc import describe
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=500)

    def __str__(self):
        return f"Post {self.title}"
