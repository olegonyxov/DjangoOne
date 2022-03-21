import datetime

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.template.response import TemplateResponse
from rest_framework.views import APIView
from .serializers import SignInSerializer,SignUpSerializer
from .models import User, M_UserManager


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
        dob = request.POST['dob']
        User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password'],
            email=request.POST['email'],
            dob=datetime.datetime.strptime(dob, "%Y-%m-%d"))
        return HttpResponse(f"Success")

    else:
        response = TemplateResponse(request, "sign_up_form.html", {'sign_up_url': '/auth/sign_up/'})
        return response


def log_out(request):
    logout(request)


class AuthSignIn(APIView):

    def post(self, request, format=None):
        token = None
        user_data=SignInSerializer(data=request.data)
        if user_data.is_valid(raise_exception=True):
            try:
                token = M_UserManager().get_user__token_by_credentials(
                    username=user_data.validated_data["username"],
                    password=user_data.validated_data["password"])
            except User.DoesNotExist:
                raise Exception("User Not Found")
            if not token:
                return HttpResponse("incorrect credentialss")
        return HttpResponse(f'Token: {token[0]}')

class AuthSignUp(APIView):

    def post(self, request, format=None):
        user_data = SignUpSerializer(data=request.data)

        if user_data.is_valid():
            M_UserManager().create_user_api(
                username=user_data.validated_data["username"],
                password=user_data.validated_data["password"],
                email=user_data.validated_data["email"],
                dob=user_data.validated_data["dob"]
            )
        return HttpResponse("User Registered , Login please")
