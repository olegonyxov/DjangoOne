from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    print(request)
    return HttpResponse("Hello, world. You're at the first_app index.")

def hello(request):
    return HttpResponse("Hello, world.")
