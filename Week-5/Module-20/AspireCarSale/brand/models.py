from django.db import models


class BrandModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    established = models.DateField()
    slug = models.SlugField(max_length=200, null=True, blank=True, unique=True)

    def __str__(self):
        return self.name