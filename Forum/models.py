from django.db import models

# Create your models here.
class Post(models.Model):
    """A Post a User Makes"""
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.CharField(max_length=100)
    def __str__(self):
        """Return a string representation of the model."""
        return str(self.id) + ". " + self.title
