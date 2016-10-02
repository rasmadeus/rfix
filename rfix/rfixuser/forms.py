from django import forms
from rfix.rfixuser.models import RfixUser


class Login(forms.ModelForm):
    class Meta:
        model = RfixUser
        fields = ['username', 'password']
