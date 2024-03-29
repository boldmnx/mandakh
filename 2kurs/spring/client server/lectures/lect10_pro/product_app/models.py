from django.db import models

# Create your models here.


class Category(models.Model):
    cname = models.CharField(max_length=255)
    cdesc = models.CharField(max_length=255)

    class Meta:
        db_table = 'tbl_category'

    def __str__(self):
        return self.cname


class Product(models.Model):
    pname = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    pdesc = models.CharField(max_length=255)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tbl_product'

    def __str__(self):
        return self.pname
