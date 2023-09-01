from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class RegistrationForm(UserCreationForm):
    profile_image = forms.ImageField(required=False, help_text="Upload a profile image")
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        if self.cleaned_data.get('profile_image'):
            user_profile = UserProfile(user=user, profile_image=self.cleaned_data['profile_image'])
            user_profile.save()
        return user
