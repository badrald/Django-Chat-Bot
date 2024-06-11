from django import forms
from .models import Profile,User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        )





class EditUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ("user",)
