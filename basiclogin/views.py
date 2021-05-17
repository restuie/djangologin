#from django.core.checks import messages
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
# Create your views here.
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from basiclogin.verification import verification
from django.contrib.sessions.models import Session
from . import models, forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.models import User
from json import dump, dumps

def login(request):
    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            login_name=request.POST['username'].strip()
            login_password=request.POST['password']
            user = authenticate(username=login_name, password=login_password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    print("success")
                    messages.add_message(request, messages.SUCCESS, '成功登入了')
                    return redirect('/')
                else:
                    messages.add_message(request, messages.WARNING, '帳號尚未啟用')
            else:
                messages.add_message(request, messages.WARNING, '登入失敗')
        else:
            messages.add_message(request, messages.INFO,'請檢查輸入的欄位內容')
    else:
        login_form = forms.LoginForm()
    return render(request, 'login.html', locals())


def register(request):
    if request.method == "POST":
        register_form = forms.RegisterForm(request.POST)
        if register_form.is_valid():
            register_name=request.POST['username'].strip()
            register_password=request.POST['password']
            register_check_password=request.POST['check_password']
            if register_password == register_check_password:
                user = authenticate(username=register_name)
                if user is None:
                    User.objects.create_user(username=register_name, password=register_password)
                    messages.add_message(request, messages.SUCCESS, '帳號註冊成功')
                    return redirect('/login')
                else:
                    messages.add_message(request, messages.WARNING, '已有相同的使用者')
            else:        
                messages.add_message(request, messages.WARNING, '請再次輸入確認密碼')
        else:
            messages.add_message(request, messages.INFO,'請檢查輸入的欄位內容')
    else:
        register_form = forms.RegisterForm()
    return render(request, 'register.html', locals())

def index(request, pid=None, del_pass=None):
    if request.user.is_authenticated:
        username = request.user.username
        try:
            user = models.User.objects.get(username=username)
            diaries = models.rfidtag.objects.filter(user=user).order_by('-ddate')
        except:
            pass

    messages.get_messages(request)
    return render(request, 'index.html', locals())

def rfidinfo(request):
    if request.user.is_authenticated:
        username = request.user.username
        try: 
            user = User.objects.get(username=username)
            wifiinfo = models.wifi.objects.get(user=user)
            wifiname = wifiinfo.wifiname
            wifipassword = wifiinfo.wifipassword   

        except:
            fail = 'fail'
    return render(request, 'rfid.html', locals())

@login_required(login_url='/login/')
def userinfo(request):
    if request.user.is_authenticated:
        username = request.user.username
        try:
            user = User.objects.get(username=username)
            userinfo = models.wifi.objects.get(user=user)
        except:
            fail = 'fail'
    return render(request, 'userinfo.html', locals())

def logout(request):
    auth.logout(request)
    messages.add_message(request, messages.INFO, "成功登出了")
    return redirect('/')

