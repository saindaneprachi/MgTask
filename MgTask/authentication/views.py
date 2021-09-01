import json
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth import login, logout
from django.views.decorators.http import require_http_methods
from django.core.mail import send_mail
from .models import UserSignUp
from MgTask.settings import EMAIL_HOST_USER


# Create your views here.



@require_http_methods(["POST"])
def login_view(request):

    params = json.loads(request.body)
    queryset = User.objects.filter(
        username=params['username']
    )

    if queryset.exists():
        user = queryset.last()
        is_password_correct = user.check_password(params['password'])
        if is_password_correct:
            login(request, user)

            data = {
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
                "last_login": user.last_login,
                "data_of_joining": user.date_joined,
            }

            return JsonResponse({
                "message": "Success",
                "status": True,
                "data": data
            })
        else:
            return JsonResponse({
                "message": "Incorrect Password",
                "status": False
            })

    else:
        return JsonResponse({
            "message": "User Not Found",
            "status": False
        })


@require_http_methods(["POST"])
def logout_view(request):
    logout(request)
    return JsonResponse({
            "message": "Logout Successfully.",
            "status": True
        })


@require_http_methods(["POST"])
def signup_user_account(request):

    params = json.loads(request.body)
    otp = 1234

    instance = UserSignUp.objects.create(
        username=params.get('username'),
        first_name=params.get('first_name'),
        last_name=params.get('last_name'),
        email=params.get('email'),
        otp=otp
    )
    message = f'Your account creation otp is {otp}.'
    send_mail(
        'ClickUP Account Creation',
        message,
        EMAIL_HOST_USER,
        [params.get('email')],
        fail_silently=False,
    )
    return JsonResponse({
        "message": "OTP Sent on email",
        "status": True,
        "data": instance.get_json()
    })


@require_http_methods(["POST"])
def verify_signup_otp_and_create_user(request):
    params = json.loads(request.body)
    _id = params.get('id')
    input_otp = params.get('otp')
    username = params.get('username')
    password = params.get('password')
    confirm_password = params.get('confirm_password')

    if not password == confirm_password:
        return JsonResponse({
            "message": "Both password not matched",
            "status": False,
        })

    queryset: UserSignUp = UserSignUp.objects.filter(id=_id, username=username)
    if queryset.exists():
        instance = queryset.last()
        if input_otp == instance.otp:
            user_instance: User = User.objects.create(username=instance.username)
            user_instance.set_password(password)
            user_instance.first_name = instance.first_name
            user_instance.last_name = instance.last_name
            user_instance.email = instance.email
            user_instance.save()

            data = {
                "id": user_instance.id,
                "first_name": user_instance.first_name,
                "last_name": user_instance.last_name,
                "email": user_instance.email,
                "last_login": user_instance.last_login,
                "data_of_joining": user_instance.date_joined,
            }
            return JsonResponse({
                "message": "Account created successfully",
                "status": True,
                "data": data
            })
        else:
            return JsonResponse({
                "message": "Invalid OTP",
                "status": False,
            })
    else:
        return JsonResponse({
            "message": "Details not found",
            "status": False
        })

@require_http_methods(["POST"])
def forget_password(request):
    params = json.loads(request.body)
    otp = 1122
    queryset = User.objects.filter(email=params['email'])


























    input_otp = params.get('otp')
    email = params.get('email')
    queryset: UserSignUp = UserSignUp.objects.filter(email=email)

    if queryset.exists():
        instance= queryset.last()
        if input_otp == instance.otp:
            user_instance: User = User.objects.filter(email=instance.email)
            user_instance.save()

            data ={
                "id" : user_instance.id,
                "email": user_instance.email,

            }

            message = f'Your password reset otp is {otp}.'
            send_mail(
                'MgTask Account Password Reset',
                 message,
                 EMAIL_HOST_USER,
                 [params.get('email')],
                 fail_silently = False,
             )
            return JsonResponse({
                "message": "OTP sent on email",
                "status": True,
                "data": instance.get_json()
            })
        else:
            return JsonResponse({
                "message" : "Invalid OTP",
                "status" : False,
            })
    else:
        return JsonResponse({
            "message" : "User not found",
            "status": False
        })

    #     params = json.loads(request.body)
#     otp = 1122
#     queryset = User.objects.filter(
#         email=params['email'],
#         otp=otp)
#     if queryset.exists():
#         for user in queryset:
#              message = f'Your password reset otp is here {otp}'.
#              send_mail(
#             'Clickup Account Password Reset',
#              message,
#              EMAIL_HOST_USER,
#              [params.get('email')],
#              fail_silently = False,
#         )

@require_http_methods(["POST"])
def change_password(request):
    params = json.loads(request.body)
    current_password= params.get('current_password')
    new_password = params.get('new_password')
    confirm_password = params.get('confirm_password')
    queryset = User.objects.filter(username= params['username'])

    if not new_password == confirm_password :
        return JsonResponse({
            "message": "Both password doesn't match",
            "status": False,
        })
    # queryset:UserSignUp = UserSignUp.objects.filter(current_password= current_password, username=username )
    if queryset.exist():
       user = queryset.last()
       is_password_correct= user.check_password(params['current_password'])
       if is_password_correct:
          User.set_password(new_password)
          data ={
               "username": user.username,
               "current_password":user.current_password,
               "new_password": user.new_password,
               "confirm_password": user.confirm_password,
          }
          return JsonResponse({
              "message": "Password reset done",
              "status": True,
              "data": data
          })
       else:
            return JsonResponse({
                "message": "Invalid OTP",
                "status": True
            })
    else:
        return JsonResponse({
            "message": "Invalid OTP",
            "status": False
        })













