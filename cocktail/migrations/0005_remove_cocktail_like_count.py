# Generated by Django 4.0.6 on 2022-08-17 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cocktail', '0004_cocktail_like_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cocktail',
            name='like_count',
        ),
    ]
