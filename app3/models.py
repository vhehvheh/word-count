from django.db import models

# Create your models here.
class Login(models.Model):
    identity = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)
    