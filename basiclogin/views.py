from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from django.contrib import auth
from .models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from basiclogin.verification import verification

def login(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        # if 驗證成功返回 user 物件，否則返回None
        #user = auth.authenticate(username=user, password=pwd)
        user = verification(wifiname=user,wifipassword=pwd).verifity()
        if user:
            # request.user ： 當前登入物件
            auth.login(request, user)
            # return HttpResponse("OK")
            return redirect('/')
    return render(request, 'login.html')

def index(request):
    print('request.user', request.user.username)
    print('request.user', request.user.id)
    # 下面是判斷是是否是匿名
    print('request.user', request.user.is_anonymous)

    if request.user.is_anonymous:
    # if not request.user.authenticated():
        return redirect('/login')
    username = request.user.username

    return render(request, 'index.html', locals())

def register(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        
        user = User(wifiname=user, wifipassword=pwd)
        user.save()
        return HttpResponse("OK")
    return render(request, 'register.html')