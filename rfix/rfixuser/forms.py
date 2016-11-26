from django import forms
from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as tr


class Login(forms.Form):
    username = forms.CharField(label=tr('Login'))
    password = forms.CharField(label=tr('Password'), widget=forms.PasswordInput)

    def login(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        return authenticate(username=username, password=password)

    def add_login_error(self):
        self.add_error('password', tr('Your password or login is invalid'))
