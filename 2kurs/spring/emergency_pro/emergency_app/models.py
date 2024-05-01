
from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=255, blank=True)


class Customer(models.Model):
    name = models.CharField(max_length=100)
    joined_at = models.DateTimeField(auto_now_add=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
