

from django.db import models


class Branch(models.Model):
    # bid = models.AutoField(primary_key=True)
    bname = models.CharField(max_length=50)

    # class Meta:
    #     db_table = 'branches'

    def __str__(self):
        return self.bname


class Worker(models.Model):
    wname = models.CharField(max_length=50)
    bid = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.wname} ({self.bid.bname})'

# name: administrator pass: boldoo1234
