from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class RegisterUser(models.Model):
    username = models.CharField(max_length=150)
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    email = models.ForeignKey(User, on_delete=models.CASCADE)
    newpassword = models.CharField(max_length=100)
    is_verified = models.BooleanField(default= False)
    token = models.CharField(max_length=20, default=None)

def __str__(self):
    return self.username


class Login(models.Model):
    username = models.CharField(max_length=150)
    email = models.ForeignKey(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=100)

def __str__(self):
    return self.username


class ForgetPassword(models.Model):
    email = models.ForeignKey(User, on_delete=models.CASCADE)
    newpassword = models.CharField(max_length=100)

def __str__(self):
    return self.email

class ChangePassword(models.Model):
    currentpassword = models.CharField(max_length=100)
    newpassword = models.CharField(max_length=100)

def __str__(self):
    return self.currentpassword