from django.db import models
from django.contrib.auth.models import User
from category.models import Category


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ManyToManyField(Category, related_name='post_category')
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
