from django.shortcuts import render,redirect
from .forms import RegistrationForm, UserProfileEditForm, UserUpdateEditForm
from .models import UserProfile
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages  
# Create your vifews here.

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            profile_image = form.cleaned_data.get('profile_image')
            try:
                user_profile = UserProfile.objects.get(user=user)
                user_profile.profile_image = profile_image
                user_profile.save()
            except UserProfile.DoesNotExist:
                user_profile = UserProfile(user=user, profile_image=profile_image)
                user_profile.save()
            return redirect('profile')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=user_name, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Invalid User. Please try again.')

    return render(request, 'signin.html')

def user_logout(request):
    logout(request)
    return redirect('home')

def profile(request):
    if request.user.is_authenticated:
        try:
            user_profile = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            user_profile = None  
        return render(request, 'profile.html', {'user_profile': user_profile})
    else:
        return redirect('signin')
    

def edit_profile(request):
    user = request.user
    user_profile = user.userprofile
    if request.method == 'POST':
        user_form = UserUpdateEditForm(request.POST, instance=user)
        profile_form = UserProfileEditForm(request.POST, request.FILES, instance=user_profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile') 
        else:
            messages.error(request, 'There was an error updating your profile. Please correct the errors.')

    else:
        user_form = UserUpdateEditForm(instance=user)
        profile_form = UserProfileEditForm(instance=user_profile)

    return render(request, 'edit_profile.html', {'user_form': user_form, 'profile_form': profile_form})