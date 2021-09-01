from django.urls import path, include
from django.contrib import admin
from .views import *

urlpatterns = [

    path('v1/login/', login_view),
    path('v1/logout/', logout_view),
    path('v1/signup/', signup_user_account),
    path('v1/verify_signup_otp/', verify_signup_otp_and_create_user),
    path('v1/forget_password/', forget_password),
    path('v1/change_password/',change_password),

]
