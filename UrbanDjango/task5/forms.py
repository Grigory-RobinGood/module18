from django import forms
from django.core.exceptions import ValidationError


class UserRegister(forms.Form):
    username = forms.CharField(
        max_length=30,
        label='Введите логин',
        widget=forms.TextInput(attrs={'placeholder': 'Логин'})
    )
    password = forms.CharField(
        min_length=8,
        label='Введите пароль',
        widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'})
    )
    repeat_password = forms.CharField(
        min_length=8,
        label='Повторите пароль',
        widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль'})
    )
    age = forms.IntegerField(
        label='Введите свой возраст',
        max_value=999,
        widget=forms.NumberInput(attrs={'placeholder': 'Возраст'})
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        repeat_password = cleaned_data.get("repeat_password")

        if password and repeat_password and password != repeat_password:
            raise ValidationError("Пароли не совпадают.")

        return cleaned_data
