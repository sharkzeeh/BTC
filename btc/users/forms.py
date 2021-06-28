from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)  # required=True is default
    first_name = forms.CharField(max_length=20, required=True)
    last_name = forms.CharField(max_length=20, required=True)

    class Meta:
        model = User  # the model to be affected is `User`
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


# model form - allows to create a form that will work with specific database model
# in this case we want a form that will update our User model
class UserUpdateForm(forms.ModelForm):
    '''
    allows to update `username` and `email`
    '''
    email = forms.EmailField(required=True)  # required=True is default
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)

    class Meta:
        model = User  # the model to be affected is `User`
        fields = ['username', 'first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
    '''
    allows to update the profile: image
    '''
    class Meta:
        model = Profile
        fields = ['image']