

from django.db import models


# Create your models here.


class Branch(models.Model):
    bid = models.AutoField(primary_key=True)
    bname = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.bname}'


class Worker(models.Model):
    wid = models.AutoField(primary_key=True)
    wname = models.CharField(max_length=100),
    bid = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.wname} ({self.bid.bname})'
