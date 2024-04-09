from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserDetails(models.Model):
    user_site = models.URLField()
    user_mobile = models.PositiveBigIntegerField()
    user_img = models.ImageField(upload_to='uploads')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{User.last_name} овогтой {User.first_name}'
