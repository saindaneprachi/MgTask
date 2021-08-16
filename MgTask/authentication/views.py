from django.contrib.auth import authenticate,login
from django.shortcuts import render
from django.http import JsonResponse, request
from django.views.decorators.csrf import csrf_exempt
from .models import Login, ForgetPassword, ChangePassword
import json
from django.contrib.auth.models import User


# Create your views here.
@csrf_exempt
def login(request, user, login=None):
    if request.method == "GET":
        result = []
        logins = Login.objects.all()  #ORM

        for login in logins:
            data = {
                "id": login.id,     #data is variable and it is dict.type
               "username": login.username,
               "email": login.email.id,
               "password": login.password,

            }
            result.append(data)
        return JsonResponse({'message': 'Success', 'data': result})

    Username = request.POST['Username']
    Password = request.POST['Password']
    user = authenticate(request, username=Username, password=Password)
    if user is not None:
        login(request, user)
        # Redirect to a success page
        return JsonResponse({"message": "Login Successful"})
    else:
        # Return an 'invalid login' error message.
        return JsonResponse({"message" : "Login Failed"})

        # if request.method == "POST":
        #     params = json.loads(request.body)
        #     isinstance = Login.objects.create(username=params.get('username'),
        #                                      email=User.objects.get(id=params.get('email')),
        #                                      password=params.get('password'))
        #     return JsonResponse({'message': 'Success', 'data': "result"})

    if request.method == "PATCH":
        params = json.loads(request.body)
        isinstance = Login.objects.filter(email=params.get('email')).update(username='Tech world')
        return JsonResponse({'message': 'Success', 'data': "result"})

    if request.method == "DELETE":
        params = json.loads(request.body)
        isinstance = Login.objects.filter(username=params.get('username'),
                                          email=User.objects.get(id=params.get('email')),
                                          password=params.get('password')).delete()
        return JsonResponse({'message':'Success','data': "result"})


@csrf_exempt
def logout(request):
    logout(request)
    # Redirect to a success page.
    return JsonResponse({"message": "Logout Successful"})

@csrf_exempt
def forgetpassword(request):
    if request.method == "GET":
        result = []
        forgetpasswords = ForgetPassword.objects.all()  #ORM

        for forgetpassword in forgetpasswords:
            data = {
                "id": forgetpassword.id,     #data is variable and it is dict.type
                "email" : forgetpassword.email.id,
                "username" : forgetpassword.username,

            }
        result.append(data)
        return JsonResponse({'message': 'Success', 'data': "result"})


    if request.method == "POST":
        params = json.loads(request.body)
        isinstance = ForgetPassword.objects.create(username=params.get('username'),
                                         email=User.objects.get(id=params.get('email')),
                                         password=params.get('password'))
        return JsonResponse({'message': 'Success', 'data': "result"})

    if request.method == "DELETE":
        params = json.loads(request.body)
        isinstance = ForgetPassword.objects.filter(username=params.get('username'),
                                          email=User.objects.get(id=params.get('email')),
                                          password=params.get('password')).delete()
        return JsonResponse({'message':'Success','data': "result"})
    
    if request.method == "PATHCH":
        params = json.loads(request.body)
        isinstance = ForgetPassword.objects.filter(email=params.get('email')).update(password='1234')
        return JsonResponse({'message': 'Success', 'data': "result"})


@csrf_exempt
def changepassword(request):
    if request.method == "GET":
        result = []
        changepasswords = ChangePassword.objects.all()  # ORM

        for changepassword in changepasswords:
            data = {
                "id": changepassword.id,  # data is variable and it is dict.type
                "email": changepassword.email.id,
                "currentpassword": changepassword.changepassword,
                "newpassword": changepassword.changepassword

            }
        result.append(data)
        return JsonResponse({'message': 'Success', 'data': "result"})

    if request.method == "POST":
        params = json.loads(request.body)
        isinstance = ChangePassword.objects.create(email=User.objects.get(id=params.get('email')),
                                                   currentpassword=params.get('password'),newpassword=params.get('newpassword'))
        return JsonResponse({'message': 'Success', 'data': "result"})

    if request.method == "DELETE":
        params = json.loads(request.body)
        isinstance = ChangePassword.objects.filter(email=User.objects.get(id=params.get('email')),
                                                   currentpassword=params.get('password'),newpassword=params.get('newpassword')).delete()
        return JsonResponse({'message': 'Success', 'data': "result"})

    if request.method == "PATHCH":
        params = json.loads(request.body)
        isinstance = ChangePassword.objects.filter(email=params.get('email')).update(newpassword='1234')
        return JsonResponse({'message': 'Success', 'data': "result"})

        