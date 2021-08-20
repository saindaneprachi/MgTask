from django.contrib.auth import authenticate,login
from django.shortcuts import render
from django.http import JsonResponse, request
from django.views.decorators.csrf import csrf_exempt
from .models import Login, ForgetPassword, ChangePassword, RegisterUser
import json
import random, math
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import  get_current_site
from django.core.mail import send_mail
from django.conf import settings



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
    if request.method == 'POST':
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
def register_user(request):
    if request.method == "GET":
        result = []
        register_users = RegisterUser.objects.all()  #ORM

        for register_user in register_users:
            data = {
                "id": register_user.id,     #data is variable and it is dict.type
                "username" : register_user.username,
                "firstname" : register_user.firstname,
                "lastname": register_user.lastname,
                "email": register_user.email.id,
                "newpassword": register_user.newpassword,

            }
        result.append(data)
        return JsonResponse({'message': 'Success', 'data': "result"})

    if request.method == "POST":
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        newpassword = request.POST.get('newpassword')
        user = RegisterUser(username = username ,firstname= firstname,
                            lastname = lastname, email = email,
                            newpassword = newpassword)
        domain_name = get_current_site(request).domain
        token =  str(random.random()).split('.')[1]
        user.token = token
        link = f'http://{domain_name}/verify/{token}'
        send_mail(
            'Email verification',
            f'please click{link} to verify your email!',
            settings.EMAIL_host_USER,
            [email],
            fail_silently=False,
        )
        return JsonResponse({'message' : 'The email has been sent!'})
        #http://my-doamin.com/verify/<token>
        # params = json.loads(request.body)
        # isinstance = ForgetPassword.objects.create(username=params.get('username'),
        #                                            firstname=params.get('firstname'),
        #                                            lastname=params.get('lastname'),
        #                                            email=User.objects.get(id=params.get('email')),
        #                                            newpassword=params.get('newpassword'))
        # user = RegisterUser(username=username, firstname=firstname,
        #                     lastname=lastname, email=email,
        #                     newpassword=newpassword)

@csrf_exempt
def verify (request,token):
   user = RegisterUser.objects.filter(token = token)
   try:
       if user:
           user.is_verified = True
           msg = "Your email has beeen verified"
           return JsonResponse({'msg' : msg})
   except:
       return JsonResponse({'message':'Check your token'})

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













