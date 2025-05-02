from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class UserCreationFrom(UserCreationForm):
    class Meta:
        models = User
        fields = ("email", "full_name")