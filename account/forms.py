from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile, Skill, Resume

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

class ProfileImageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_image']
        
class UserUpdateEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {
            'username': 'Username',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'email': forms.EmailInput(attrs={'class': 'form-control mb-2'}),
        }

class UserProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_image']
        labels = {
            'profile_image': 'Profile Image',
        }
        widgets = {
            'profile_image': forms.ClearableFileInput(attrs={'class': 'form-control mb-2'}),
        }
        
class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'percentage']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'percentage': forms.NumberInput(attrs={'class': 'form-control mb-2'}),  
        }

    def clean_percentage(self):
        percentage = self.cleaned_data.get('percentage')
        if percentage > 100:
            raise forms.ValidationError("Percentage cannot exceed 100%.")
        return percentage
    
class EditSkill(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'percentage']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'percentage': forms.NumberInput(attrs={'class': 'form-control mb-2'}),  
        }
        

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['name', 'file']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control mb-2'}),
        }




