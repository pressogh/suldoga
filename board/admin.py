from django.contrib import admin
from .models import Board

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'body', 'date']
    list_display_links = ['title','author']
    list_per_page = 10

# Register your models here.
