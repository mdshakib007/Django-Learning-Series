from datetime import datetime
from django.db import models
from categories.models import Category
from author.models import Author

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    time = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.title

        