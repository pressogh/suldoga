from django.db import models

# Create your models here.
class CocktailCocktail(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20)
    eng_name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    image = models.CharField(max_length=100)
    alcohol = models.CharField(max_length=20)
    taste = models.CharField(max_length=20)
    base = models.CharField(max_length=20)
    match_food = models.CharField(max_length=20)
    type = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'cocktail_cocktail'