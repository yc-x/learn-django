from django.db import models

# Create your models here.

class Notes(models.Model):
    title = models.CharField(max_length=140)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

