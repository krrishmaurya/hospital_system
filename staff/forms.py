from django import forms

class Login(forms.Form):
    user_name=forms.CharField(max_length=30)
    password=forms.CharField(widget=forms.PasswordInput())
    