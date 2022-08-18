from django import forms
from .models import Post


class PostUploadForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'user', 'content']
        

        widgets = {
            "username": forms.TextInput(attrs={
                'placeholder': '제목',
                'name': 'title'
            }),
            "password": forms.Textarea(attrs={
                'placeholder': '내용',
                'name': 'content',
            }),
        }
