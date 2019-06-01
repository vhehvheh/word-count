from django.shortcuts import render
from .models import Login
# Create your views here.

def login(request):
    return render(request, "login/login.html")

def main(request):
    return render(request, "login/main.html")

def check(request):
    user_id = request.GET.get('id')
    user_pwd = request.GET.get('password')
    print(user_id)
    print(user_pwd)
    user_infos = Login.objects.all()
    for user_info in user_infos :
        if(user_info.identity == user_id and user_info.password == user_pwd):
            text = "로그인"
            break

        else :
            text = "실패"

    context = {'text' : text}

    return render(request, "login/check.html",context)