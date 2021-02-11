from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=150)
    portfolio=models.URLField(blank=True)


    def __str__(self):
        return self.name

class Userinfo(User):

    def __str__(self):
        return self.username
