from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class wifi(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    wifiname = models.CharField(max_length=20,null=False)
    wifipassword = models.CharField(max_length=20,null=False)
    def __str__(self):
        return self.user.username

class rfidtag(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    rfid = models.CharField(max_length=20,null=False)
    #ddate = models.CharField(max_length=20,null=False)
    ddate = models.DateField()
    def __str__(self):
        return "{}({})".format(self.ddate,self.user)