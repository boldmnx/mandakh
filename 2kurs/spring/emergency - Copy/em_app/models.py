from django.db import models

# Create your models here.


class Doctor(models.Model):
    name = models.CharField(blank=True, max_length=255)

    class Meta:
        db_table = 'doctor'

    def __str__(self):
        return f'{self.name}'


class Customer(models.Model):
    name = models.CharField(max_length=255, blank=True)

    class Meta:
        db_table = 'customer'

    def __str__(self):
        return f'{self.name}'
