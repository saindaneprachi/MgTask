from django.urls import path
from .import views

urlpatterns = [

    path('Login', views.Login, name='Login'),
    path('ForgetPassword', views.ForgetPassword, name='ForgetPassword'),
    path('ChangePassword', views.ChangePassword, name='ChangePassword'),
    path('RegisterUser', views.RegisterUser, name='RegisterUser'),
    path('verify/<str:token>', views.verify),

]
