

from django.db import models

# Create your models here.


class Branch(models.Model):
    bid = models.AutoField(primary_key=True)
    bname = models.CharField(max_length=50)

    class Meta:
        db_table = 'tbl_branch'

    def __str__(self):
        
        return self.bname

