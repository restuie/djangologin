from django.db import models

# Create your models here.
class User(models.Model):
    wifiname = models.CharField(max_length=20,null=False)
    wifipassword = models.CharField(max_length=20,null=True)
