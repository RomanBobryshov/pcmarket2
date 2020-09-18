from .models import Profile
from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):

    phone_number = forms.CharField(label='Номер телефону')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):

    phone_number = forms.CharField(label='Номер телефону')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторіть пароль', widget=forms.PasswordInput)

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'phone')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('city', 'address')