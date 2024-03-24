from django.db import models
from branch_app.models import Branch
# Create your models here.


class Worker(models.Model):
    wname = models.CharField(max_length=255)
    bid = models.ForeignKey(Branch, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tbl_worker'

    def __str__(self):
        return self.wname + f' ({self.bid.bname})'
