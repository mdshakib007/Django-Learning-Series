from django.db import models
from brand.models import BrandModel
from django.contrib.auth.models import User


class CarModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    released_date = models.DateField()
    quantity = models.IntegerField()
    image = models.ImageField()
    price = models.BigIntegerField()
    brand = models.ForeignKey(BrandModel, on_delete=models.CASCADE, related_name='car_brand')
    customer = models.ManyToManyField(User, null=True, blank=True)

    def __str__(self):
        return self.title

class CommentModel(models.Model):
    car = models.ForeignKey(CarModel, on_delete = models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.customer.username}"