from django.db import models
from musician.models import MusicianModel
from datetime import date

# Create your models here.
class AlbumModel(models.Model):
    album_name = models.CharField(max_length=40)
    musician = models.ForeignKey(MusicianModel, on_delete=models.CASCADE)
    RATINGS = [('1', '1 Star'), ('2', '2 Star'), ('3', '3 Star'), ('4', '4 Star'), ('5', '5 Star')]
    ratings = models.CharField(max_length=6, choices=RATINGS)
    release_date = models.DateField()

    def save(self, *args, **kwargs):
        if not self.release_date:
            self.release_date = date.today()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.album_name} - by {self.musician.first_name} {self.musician.last_name}"
