from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    GENDER_CHOICES = [
        ('M', 'MAN'),
        ('F', 'WOMAN')
    ]

    gender = models.CharField(blank=False, max_length=1, choices=GENDER_CHOICES)
    first_name = models.CharField(blank=False, max_length=20)
