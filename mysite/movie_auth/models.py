from django.contrib.auth.models import (BaseUserManager)
from django.contrib.auth.models import User
from django.db import models


class User(User):  # strange but needed
    # user = models.OneToOneField(DjangoUser, on_delete=models.CASCADE)
    dob = models.DateField()


class M_UserManager(BaseUserManager):
    def create_user(self, username, email, dob, password=None):
        if not email:
            raise ValueError("Please enter Your email")
        if User.objects.filte(email=email).exists():
            raise ValueError("Email already used")
        user = self.model(
            username=username,
            email=email,
            dob=dob
        )
        user.set_password(password)
        user.save(using=self.db)
        return user
