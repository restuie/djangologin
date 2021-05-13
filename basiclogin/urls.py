from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
app_name = "basiclogin"

urlpatterns = [
    path('', views.index, name="index"),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
]