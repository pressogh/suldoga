from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    GENDER_CHOICES = [
        ('M', 'MAN'),
        ('F', 'WOMAN')
    ]

    gender = models.CharField(blank=False, max_length=1, choices=GENDER_CHOICES)
    first_name = models.CharField(blank=False, max_length=20)


class UserSurvey(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.IntegerField(blank=True, null=True)
    sweet = models.IntegerField(blank=True, null=True)
    degree = models.IntegerField(blank=True, null=True)
