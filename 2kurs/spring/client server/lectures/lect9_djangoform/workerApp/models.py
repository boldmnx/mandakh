from django.db import models

# Create your models here.


class Branch(models.Model):
    bname = models.CharField(max_length=255)
    baddress = models.CharField(max_length=255)
    bphone = models.CharField(max_length=255)

    class Meta:
        db_table = 'tbl_branch'

    def __str__(self):
        return self.bname


class Worker(models.Model):
    wfname = models.CharField(max_length=255),
    wlname = models.CharField(max_length=255),
    wgender = models.CharField(max_length=2),
    wphone = models.CharField(max_length=255),
    bid = models.ForeignKey(Branch, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tbl_worker'

    def __str__(self):
        return f'{self.wlname[0]}. {self.wfname}'
