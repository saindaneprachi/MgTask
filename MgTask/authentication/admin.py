from django.contrib import admin
from .models import UserSignUp

# Register your models here.
@admin.register(UserSignUp)
class UserSignUpAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'email']
    list_filter = ['first_name']
    search_fields = ['first_name']

