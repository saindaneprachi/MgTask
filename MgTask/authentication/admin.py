from django.contrib import admin
from .models import Login, ForgetPassword, ChangePassword

# Register your models here.

admin.site.register(Login)
admin.site.register(ForgetPassword)
admin.site.register(ChangePassword)
