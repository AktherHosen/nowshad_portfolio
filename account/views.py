from django.shortcuts import render,redirect,get_object_or_404
from .forms import RegistrationForm, UserProfileEditForm, UserUpdateEditForm,SkillForm,EditSkill 
from .models import UserProfile, Skill
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from contact.models import ContactMessage
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

def show_skills(request):
    skills = Skill.objects.all()
    return render(request, 'show_skills.html', {'skills':skills})

def add_skill(request):
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SkillForm()
    
    return render(request, 'add_skill.html', {'form': form})

def edit_skill(request, skill_id):
    skill = get_object_or_404(Skill, pk=skill_id)

    if request.method == 'POST':
        form = EditSkill(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = EditSkill(instance=skill)

    return render(request, 'edit_skill.html', {'form': form, 'skill': skill})


def all_messages(request):
    messages = ContactMessage.objects.all()
    return render(request, 'messages.html',{'messages':messages})

def delete_message(request,message_id):
    blog = get_object_or_404(ContactMessage, id=message_id)
    blog.delete()
    return redirect('messages')