from django.db import models
from django.contrib.auth.models import User
from patient.models import Patient


class Specialization(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class Designation(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return f"{self.name}"
    

class AvailableTime(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"
    

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor')
    image = models.ImageField(upload_to="doctor/images/")
    designation = models.ManyToManyField(Designation, related_name='designation')
    specialization = models.ManyToManyField(Specialization, related_name='specialization')
    available_time = models.ManyToManyField(AvailableTime, related_name='available_time')
    fee = models.IntegerField()
    meet_link = models.URLField(max_length=100)

    def __str__(self):
        return f"Dr. {self.user.first_name} {self.user.last_name}"

STAR_CHOICES = [
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐', '⭐'),
]
class Review(models.Model):
    reviewer = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    rating = models.CharField(max_length=20, choices=STAR_CHOICES)

    def __str__(self):
        return f"Reviewer: {self.reviewer.user.first_name} | Doctor: {self.doctor.user.first_name} | Rating: {self.rating}"