from celery import shared_task   #Celery
from .models import User
import time


@shared_task()
def add(x,y):
    return (x+y)



@shared_task
def change_flag():
    User.objects.filter(is_notified=False).update(is_notified=True)
