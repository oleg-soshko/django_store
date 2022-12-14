from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Payment, Delivery


class CheckoutForm(forms.Form):
    city = forms.CharField(max_length=150, label='Город', widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(max_length=250, label='Адрес', widget=forms.TextInput(attrs={'class': 'form-control'}))
    payment_type = forms.ModelChoiceField(label='Тип оплаты', queryset=Payment.objects.all(),
                                          widget=forms.Select(attrs={'class': 'form-control'}))
    delivery_type = forms.ModelChoiceField(label='Тип доставки', queryset=Delivery.objects.all(),
                                           widget=forms.Select(attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control',
                                                                            'placeholder': 'name@example.com'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
