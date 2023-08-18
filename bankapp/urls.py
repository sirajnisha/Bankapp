
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
app_name ='bankapp'
urlpatterns = [

    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path("login",views.login,name="login"),
    path("success",views.success,name="success"),

]
