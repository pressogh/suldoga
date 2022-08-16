from django.db import models
from accounts.models import User


class Cocktail(models.Model):
    name = models.CharField(max_length=20)
    eng_name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='cocktail/')
    alcohol = models.CharField(max_length=20)
    taste = models.CharField(max_length=20)
    base = models.CharField(max_length=20)
    match_food = models.CharField(max_length=20)
    type = models.CharField(max_length=1, choices=(('C', 'Cocktail'), ('K', 'K-ocktail')))

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, through='Like', related_name='like_cocktail', blank=True)
    stars = models.ManyToManyField(User, through='Star', related_name='star_cocktail', blank=True)

    like_count = models.PositiveIntegerField(default=0)
    star_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    cocktail = models.ForeignKey(Cocktail,on_delete=models.CASCADE)

    def __str__(self):
        return self.cocktail


class Star(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    cocktail = models.ForeignKey(Cocktail,on_delete=models.CASCADE)

    def __str__(self):
        return self.cocktail

