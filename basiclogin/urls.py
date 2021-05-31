from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
app_name = "basiclogin"

urlpatterns = [
    path('', views.index, name="index"),
    #path('register', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('userinfo/',views.userinfo, name='userinfo'),
    path('register/',views.register, name='register'),
    path('rfidinfo/',views.rfidinfo,name='rfidinfo'),
    #path('delete/<str:rfidname>',views.deleterfid,name='delete'),
]