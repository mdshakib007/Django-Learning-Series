from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=20)
    bio = models.TextField()
    phone = models.CharField(max_length=16)
    
    def __str__(self):
        return self.name