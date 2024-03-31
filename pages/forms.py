from django import forms
import re
from django.contrib.auth.models import User
from .models import *


class RegistrationForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(
        label="Password", min_length=6, widget=forms.PasswordInput()
    )
    Password_confirmation = forms.CharField(
        label="Confirm Password",
        min_length=6,
        widget=forms.PasswordInput(),
    )
    email = forms.EmailField(label="Email")

    def clean_username(self):
        return self.cleaned_data[
            "username"
        ]  # Return the field's value after validation</pre>

    def clean_password(self):
        if "password" in self.changed_data:
            password = self.cleaned_data.get("password")
            Password_confirmation = self.cleaned_data.get("Password_confirmation")
            if password == (Password_confirmation and password):
                raise forms.ValidationError("Passwords do not match")
            else:
                return Password_confirmation

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("Username already exists")

    def save(self):
        User.objects.create_user(
            username=self.cleaned_data["username"],
            email=self.cleaned_data["email"],
            password=self.cleaned_data["password"],
        )
