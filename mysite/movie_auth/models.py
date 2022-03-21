from django.contrib.auth.models import (BaseUserManager)
from django.contrib.auth.models import User
from django.db import models
from rest_framework.authtoken.models import Token


class User(User):  # strange but needed
    # user = models.OneToOneField(DjangoUser, on_delete=models.CASCADE)
    dob = models.DateField()


class M_UserManager(BaseUserManager):
    def create_user(self, username, email, dob, password=None):
        if not email:
            raise ValueError("Please enter Your email")
        if User.objects.filter(email=email).exists():
            raise ValueError("Email already used")
        user = self.model(
            username=username,
            email=email,
            dob=dob
        )
        user.set_password(password)
        user.save(using=self.db)


        return user

    def get_user__token_by_credentials(self,username,password):
        user = User.objects.get_by_natural_key(username=username)
        if user.check_password(password):

            return Token.objects.get_or_create(user=user)

    def create_user_api(self,username, email, dob, password=None):
        user = User.objects.create_user(username= username,
                                        password=password,
                                        email=email,
                                        dob=dob
                                        )
        return user
