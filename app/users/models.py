from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """
    Manager for user profiles
    """

    def create_user(self, name, phone, password=None):
        """Create a new UserProfile"""
        if not phone:
            raise ValueError("Phone number is required field")

        user = self.model(name=name, phone=phone)
        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self, name, phone, password):
        """Create a new superuser"""
        user = self.create_user(name, phone, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    Database model for users in the system
    """
    name = models.CharField(max_length=255, null=False)
    phone = models.CharField(max_length=25, unique=True, db_index=True, null=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return f"{self.name}"
