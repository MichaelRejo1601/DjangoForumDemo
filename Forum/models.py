from django.db import models

# Create your models here.
class Post(models.Model):
    """A Post a User Makes"""
    date = models.DateField()
    time = models.TimeField()
    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.CharField(max_length=100)
    def __str__(self):
        """Return a string representation of the model."""
        return self.title
