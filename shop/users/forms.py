from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm


from users.models import User


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationsForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput())
    image = forms.ImageField(widget=forms.FileInput(), required=False)
    username = forms.CharField(widget=forms.TextInput())
    email = forms.CharField(widget=forms.TextInput())

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image', 'username', 'email')
