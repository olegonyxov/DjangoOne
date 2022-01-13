from django.http import HttpResponse
from django.shortcuts import render
from first_app.models import Movie


def index(request):
    return HttpResponse("Hello, world. You're at the first_app index.")


def hello(request):
    return HttpResponse("Hello, world.")


def movies_all(request):
    get_all = Movie.objects.all()
    return render(request, "movies_all.html", context={'get_all': get_all})


def movies_top_ten(request):
    get_top = Movie.objects.order_by('-user_rating')[:10]
    return render(request, "movies_all.html", context={'get_all': get_top})


def movies_top_input(request, top_input=1):
    get_count = Movie.objects.order_by('-user_rating')[:top_input]
    return render(request, "movies_all.html", context={'get_all': get_count})


def movies_info(request, input_title):
    movie = Movie.objects.get(title=input_title)
    other_info = movie.description, movie.pub_date, movie.url, movie.runtime
    output = movie, *other_info
    return render(request, "movies_all.html", context={'get_all': output})


def movie_rate_up(request, input_title):
    movie = Movie.objects.get(title=input_title)
    if movie.user_rating >= 100:
        pass
    else:
        movie.user_rating += 1
        movie.save()
    return HttpResponse("Thank You For Voting")


def movie_rate_down(request, input_title):
    movie = Movie.objects.get(title=input_title)
    if movie.user_rating >= 0:
        pass
    else:
        movie.user_rating -= 1
        movie.save()
    return HttpResponse("Thank You For Voting")
