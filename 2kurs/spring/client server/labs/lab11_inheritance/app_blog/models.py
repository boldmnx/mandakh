from django.db import models

# Create your models here.


class Torol(models.Model):
    tname = models.CharField(max_length=255)

    class Meta:
        db_table = 'tbl_torol'

    def __str__(self):
        return self.tname


class Blog(models.Model):
    bname = models.CharField(max_length=255)
    bcontent = models.CharField(max_length=2500, null=True)
    bdate = models.DateField(auto_now_add=True)
    btorol = models.ForeignKey(Torol, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tbl_blog'

    def __str__(self):
        return f'{self.bname} /{self.btorol.tname}/'
