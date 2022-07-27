from django import forms
from .models import User
from django.contrib.auth import authenticate


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'gender']

        labels = {
            'username': 'ID',
            'password': 'PASSWORD',
            'first_name': 'NAME',
            'gender': 'GENDER'
        }
        widgets = {
            "username": forms.TextInput(attrs={
                'placeholder': '아이디를 입력하세요',
                'name': 'username',
                'style': 'font-size: 18px; height: 24px',
                'class': 'form-item-input'
            }),
            "password": forms.PasswordInput(attrs={
                'placeholder': '숫자, 영문 포함 8자리 이상',
                'name': 'password',
                'style': 'font-size: 18px; height: 24px',
                'class': 'form-item-input'
            }),
            "first_name": forms.TextInput(attrs={
                'placeholder': '닉네임을 입력하세요',
                'name': 'name',
                'style': 'font-size: 18px; height: 24px',
                'class': 'form-item-input',
            }),
            "gender": forms.RadioSelect()
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()
        return user

    def clean(self):
        super(RegisterForm, self).clean()

        password = self.cleaned_data.get('password')

        if len(password) < 8:
            self._errors['password'] = self.error_class(['숫자, 영문 포함 8자리 이상'])

        return self.cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(label="ID", widget=forms.TextInput(attrs={
            'placeholder': '아이디를 입력하세요',
            'name': 'username',
            'style': 'font-size: 18px; height: 24px',
            'class': 'form-item-input'
        })
    )
    password = forms.CharField(label="PASSWORD", widget=forms.PasswordInput(attrs={
            'placeholder': '숫자, 영문 포함 8자리 이상',
            'name': 'password',
            'style': 'font-size: 18px; height: 24px',
            'class': 'form-item-input'
        })
    )

    def clean(self):
        super(LoginForm, self).clean()

        print(self.cleaned_data)
        password = self.cleaned_data.get('password')

        if len(password) < 8:
            self._errors['password'] = self.error_class(['숫자, 영문 포함 8자리 이상'])

        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user
