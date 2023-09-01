from django.shortcuts import render,redirect
from .forms import RegistrationForm
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