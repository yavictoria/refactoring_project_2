from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.core.exceptions import ValidationError
from .models import User, Pin

# DRY: всі підписи — константи
PASSWORD_LABEL = "Пароль"
PASSWORD2_LABEL = "Повторіть пароль"

# pylint: disable=too-many-ancestors
class SignUpForm(UserCreationForm):
    """
    Форма для реєстрації користувача.
    """
    email = forms.EmailField(label="Електронна пошта", required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'Електронна пошта'
    }))
    username = forms.CharField(label="Логін", widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Логін'
    }))
    password1 = forms.CharField(label=PASSWORD_LABEL, widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': PASSWORD_LABEL
    }))
    password2 = forms.CharField(label=PASSWORD2_LABEL, widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': PASSWORD2_LABEL
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("Цей email вже використовується.")
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError("Цей логін вже використовується.")
        return username

# pylint: disable=too-many-ancestors
class CustomUserCreationForm(UserCreationForm):
    """
    Адмін-форма для створення користувача.
    """
    password1 = forms.CharField(label=PASSWORD_LABEL, widget=forms.PasswordInput)
    password2 = forms.CharField(label=PASSWORD2_LABEL, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class CustomUserChangeForm(UserChangeForm):
    """
    Адмін-форма для редагування користувача.
    """
    class Meta:
        model = User
        fields = ('username', 'email', 'name', 'desc', 'pfp')

# pylint: disable=too-many-ancestors
class CustomLoginForm(AuthenticationForm):
    """
    Форма для авторизації користувача.
    """
    username = forms.CharField(label="Логін", widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Логін'
    }))
    password = forms.CharField(label=PASSWORD_LABEL, widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': PASSWORD_LABEL
    }))

# pylint: disable=too-many-ancestors
class PinForm(forms.ModelForm):
    """
    Форма для створення піну.
    """
    class Meta:
        model = Pin
        fields = ['title', 'desc', 'pic']

    def clean_pic(self):
        pic = self.cleaned_data.get('pic', None)
        if pic:
            # Перевірка розміру (max 2MB)
            if pic.size > 2 * 1024 * 1024:
                raise ValidationError("Зображення має бути не більше 2MB.")
            # Перевірка формату
            if not pic.content_type.startswith('image/'):
                raise ValidationError("Дозволені лише зображення.")
        return pic

# pylint: disable=too-many-ancestors
class EditProfileForm(forms.ModelForm):
    """
    Форма для редагування профілю користувача.
    """
    class Meta:
        model = User
        fields = ['name', 'desc', 'pfp']
