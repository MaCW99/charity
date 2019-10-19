from django import forms
from django.core.validators import validate_email


class RegisterForm(forms.Form):
    first_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"placeholder": "Imię"})
    )
    last_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"placeholder": "Nazwisko"})
    )
    email = forms.CharField(
        max_length=100,
        validators=[validate_email],
        widget=forms.TextInput(attrs={"placeholder": "Email"}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Hasło"})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Powtórz hasło"})
    )


class LoginForm(forms.Form):
    username = forms.CharField(
        validators=[validate_email],
        widget=forms.TextInput(attrs={"placeholder": "Email"}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Hasło"})
    )
