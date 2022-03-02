from django.db import models

from django.contrib.auth.models import User as DjangoUser

class User(DjangoUser):
    # user = models.OneToOneField(DjangoUser, on_delete=models.CASCADE)
    dob= models.DateField()