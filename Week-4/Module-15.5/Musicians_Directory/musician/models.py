from django.db import models

# Create your models here.
class MusicianModel(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField()
    phone = models.CharField(max_length=16)
    instrument_type = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"