# Generated by Django 4.0.6 on 2022-08-18 08:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cocktail', '0002_cocktail_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='cocktail',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cocktail',
            name='like_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
