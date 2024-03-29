from django.db import models

# Create your models here.


class Category(models.Model):
    cname = models.CharField(max_length=255)

    class Meta:
        db_table = 'category_tbl'

    def __str__(self):
        return self.cname


class News(models.Model):
    nname = models.CharField(max_length=255)
    npara = models.CharField(null=True, max_length=255)
    nchoose = models.CharField(max_length=5, default='', choices={
                               '': '', 'man': 'Эр', 'woman': 'Эм', 'other': 'Бусад'})
    nognoo = models.DateField(auto_now_add=True)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = 'news_tbl'

    def __str__(self):
        return f'{self.nname} /{self.cat.cname}/'
