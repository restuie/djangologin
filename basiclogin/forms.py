from django import forms
from . import models
class LoginForm(forms.Form):
    username = forms.CharField(label='姓名', max_length=10)
    password = forms.CharField(label='密碼', widget=forms.PasswordInput())

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=10)
    password = forms.CharField(max_length=10)
    check_password = forms.CharField(max_length=10)

class RFIDForm(forms.Form):
    rfidname = forms.CharField(max_length=10)