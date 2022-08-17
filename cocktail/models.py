from django.db import models


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

    def __str__(self):
        return self.name
