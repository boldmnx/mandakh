from django.db import models
from django.contrib.auth.models import User


class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # user model-н field-үүдийг ашиглахаас гадна нэмэлт user_site, user_pic
    # гэсэн талбарууд нэмж өгч байна.
    user_site = models.URLField(blank=True)
    user_pic = models.ImageField(upload_to='media/profile_pics', blank=True)

    def __str__(self):
        return self.user.username
