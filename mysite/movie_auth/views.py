import datetime

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.template.response import TemplateResponse
from .models import User
def sign_in(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse(f"Success")
        else:
            return HttpResponse("Invalid login or password", status=403)
    else:
        response = TemplateResponse(request, "sign_in_form.html", {'auth_url': '/auth/'})
        return response



def sign_up(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        dob = request.POST['dob']
        User.objects.create_user(
            username=username,
            password=password,
            email=email,
            dob=datetime.datetime.strptime(dob, "%Y-%m-%d"))
        return HttpResponse(f"Success")

    else:
        response = TemplateResponse(request, "sign_up_form.html", {'sign_up_url': '/auth/sign_up/'})
        return response

def log_out(request):
    logout(request)

