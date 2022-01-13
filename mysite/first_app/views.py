from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import loader
from first_app.models import Movie


def index(request):
    return HttpResponse("Hello, world. You're at the first_app index.")

def hello(request):
    return HttpResponse("Hello, world.")

def movies_all(request):
    get_all=Movie.objects.all()
    return render(request,"movies_all.html",context={'get_all':get_all})
def movies_top_ten(request):
    get_top = Movie.objects.order_by('-user_rating')[:10]
    return render(request, "movies_all.html", context={'get_all': get_top})
def movies_top_input(request,top_input=1):
     get_count = Movie.objects.order_by('-user_rating')[:top_input]
     return render(request, "movies_all.html", context={'get_all': get_count})


