from django.db import models
from django.contrib.auth.models import ( BaseUserManager, AbstractBaseUser )
from django.contrib.auth.models import User as DjangoUser


class User(DjangoUser):
    # user = models.OneToOneField(DjangoUser, on_delete=models.CASCADE)
    dob= models.DateField()

class M_UserManager(BaseUserManager):
    def create_user(self, username, email, dob, password=None):
        if not email:
            raise ValueError("Please enter Your email")
        user =self.model(
            username=username,
            email=email,
            dob=dob
        )

        user.set_password(password)
        user.save(using=self.db)
        return user