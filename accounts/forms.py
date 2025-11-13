from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreation(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email", "username", "name")


class CustomUserchangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("email", "username", "name")
