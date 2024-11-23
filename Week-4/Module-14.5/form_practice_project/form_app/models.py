from django.db import models

# Create your models here.
class MDModel(models.Model):
    auto_field = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.TextField()
    birthday = models.DateField()
    boolean_field = models.BooleanField()
    file_field = models.FileField(upload_to='files/')
    url_field = models.URLField()
    RATING = {
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
    }
    rating = models.CharField(max_length=5, choices=RATING)
