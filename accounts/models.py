# from django.db import models
# from django.contrib.auth.models import AbstractUser
# # Create your models here.
#
# from django.contrib.auth.base_user import BaseUserManager
# #from django.utils.translation import ugettext_lazy as _
#
#
# class CustomUserManager(BaseUserManager):
#     """
#     Custom user model manager where email is the unique identifiers
#     for authentication instead of usernames.
#     """
#     def create_user(self, phone, password, **extra_fields):
#         """
#         Create and save a User with the given email and password.
#         """
#         if not phone:
#             raise ValueError('The Email must be set')
#         phone = self.normalize_email(phone)
#         user = self.model(phone=phone, **extra_fields)
#         user.set_password(password)
#         user.save()
#         return user
#
#     def create_superuser(self, phone, password, **extra_fields):
#         """
#         Create and save a SuperUser with the given email and password.
#         """
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_active', True)
#
#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')
#         return self.create_user(phone, password, **extra_fields)
#
# class User(AbstractUser):
#     username = None
#     phone = models.IntegerField('phone', unique=True)
#     image = models.ImageField()
#     USERNAME_FIELD = 'phone'
#     REQUIRED_FIELDS = ['phone']
#
#     objects = CustomUserManager()