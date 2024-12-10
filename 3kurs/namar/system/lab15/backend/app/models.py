from django.db import models

# Create your models here.
class Student (models.Model):
    stlname = models.CharField(max_length=100)
    stfname = models.CharField(max_length=100)
    stcode = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    born = models.CharField(null=True, blank=True,max_length=250)
    email = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, default='', choices={
                               '': '', 'man': 'Эрэгтэй', 'woman': 'Эмэгтэй', 'other': 'Бусад'})
    phone = models.CharField(max_length=8)
    username = models.CharField(max_length=50)

    # related_model = models.ForeignKey(RelatedModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.stfname
    
    class Meta:
        db_table = 'student'