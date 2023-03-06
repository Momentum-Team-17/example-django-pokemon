from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    # add any additional fields you want for your User here
    age = models.IntegerField(blank=True, null=True)
