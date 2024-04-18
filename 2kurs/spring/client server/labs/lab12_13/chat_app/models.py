from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user_img = models.ImageField(blank=True, upload_to='media')
    user_site = models.URLField(blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'UserProfile'

    # def __str__(self):
    #     return f'{self.user.last_name} овогтой {self.user.first_name}'
