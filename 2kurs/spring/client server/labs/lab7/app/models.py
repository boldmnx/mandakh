

from django.db import models


# Create your models here.


class Branch(models.Model):
    bname = models.CharField()

    def __str__(self):
        return f'{self.bname}'


class Worker(models.Model):
    bid = models.ForeignKey(Branch, on_delete=models.CASCADE)
    wname = models.CharField(),

    def __str__(self):
        return f'{self.wname} ({self.bid.bname})'
