from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    SUPERUSER = 'superuser'
    ADMIN = 'admin'
    LIBRARIAN = 'librarian'
    CLIENT = 'client'

    USER_TYPES = [
        (SUPERUSER, 'Superuser'),
        (ADMIN, 'Administrator'),
        (LIBRARIAN, 'Librarian'),
        (CLIENT, 'Client'),
    ]

    user_type = models.CharField(max_length=10, choices=USER_TYPES, default=CLIENT)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'Usuarios'
