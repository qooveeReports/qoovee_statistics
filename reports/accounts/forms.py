from django import forms
from profiles.models import Profile


class Registrations(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Profile
        fields = ('username', 'password', 'email', )
