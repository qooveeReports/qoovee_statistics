from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db import models


class Profile(AbstractUser):
    phone = models.IntegerField(null=True, blank=True)
    photo = models.ImageField('media/')


    class Meta:
        swappable = 'AUTH_USER_MODEL'
