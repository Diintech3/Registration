from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser

class RegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=150)  # Username field add kiya
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password']  # Username add kiya

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match.")

        return cleaned_data

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username")  # Email ki jagah username
