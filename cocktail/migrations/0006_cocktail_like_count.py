# Generated by Django 4.0.6 on 2022-08-18 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cocktail', '0005_remove_cocktail_like_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='cocktail',
            name='like_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
