from django import forms
from django.contrib import admin
from basiclogin import models
# Register your models here.
admin.site.register(models.wifi)
admin.site.register(models.rfidtag)