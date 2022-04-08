from celery import shared_task   #Celery
from .models import User


def get_queryset():
    return User.objects.filter(is_notified=False)

@shared_task()
def add(x,y):
    return (x+y)


@shared_task
def change_flag(queryset=get_queryset()):
    queryset.update(is_notified=True)
    return queryset.filter(is_notified=False).count()
