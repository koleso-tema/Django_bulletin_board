from allauth.account.forms import LoginForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group

from accounts.models import UserCode


class UserCodeForm(forms.ModelForm):
    code = forms.CharField(label="Код", help_text='Введите код для верификации')

    class Meta:
        model = UserCode
        fields = (
            "code",
        )


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email")

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )


#
class CustomSignupForm(SignUpForm):
    def save(self, request):
        user = super().save(request)
        authors_users = Group.objects.get(name="authors")
        user.groups.add(authors_users)
        return user


class LogInForm(LoginForm):
    password = forms.CharField(label='Пароль')
    email = forms.EmailField(label='Электронный адрес')
