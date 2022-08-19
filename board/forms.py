from django import forms
from .models import Post


class PostUploadForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

        widgets = {
            "username": forms.TextInput(attrs={
                'placeholder': 'title',
                'name': 'title'
            }),
            "password": forms.Textarea(attrs={
                'placeholder': '내용',
                'name': 'content',
            }),
        }


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
