from django.db import models
from django.contrib.auth.models import AbstractUser

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, email, first_name,contact_number, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name = first_name,
            contact_number = contact_number
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, contact_number, password, first_name):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            contact_number=contact_number,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractUser):

    email = models.EmailField(max_length=300, unique=True, null = False)
    first_name = models.CharField(max_length=200, null = False)
    contact_number = models.CharField(max_length= 200, null = False)
    otp_verified = models.BooleanField(default=False)
    username = None
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "contact_number"]

    objects = MyUserManager()