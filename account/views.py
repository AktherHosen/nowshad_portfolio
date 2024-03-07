from django.shortcuts import render,redirect,get_object_or_404
from .forms import RegistrationForm, UserProfileEditForm, UserUpdateEditForm,SkillForm,EditSkill, ResumeForm
from .models import UserProfile, Skill, Resume
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
            return redirect('dashboard')
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
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid User. Please try again.')

    return render(request, 'signin.html')

def user_logout(request):
    logout(request)
    return redirect('home')

def dashboard(request):
    if request.user.is_authenticated:
        try:
            user_profile = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            user_profile = None  
        return render(request, 'dashboard.html', {'user_profile': user_profile})
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

    return render(request, 'edit_profile.html', {'user_form': user_form, 'profile_form': profile_form, 'user_profile':user_profile})

def show_skills(request):
    skills = Skill.objects.all()
    user_profile = request.user.userprofile
    return render(request, 'show_skills.html', {'skills':skills, 'user_profile':user_profile})

def add_skill(request):
    user_profile = request.user.userprofile
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SkillForm()
    
    return render(request, 'add_skill.html', {'form': form, 'user_profile':user_profile})

def edit_skill(request, skill_id):
    skill = get_object_or_404(Skill, pk=skill_id)
    user_profile = request.user.userprofile
    if request.method == 'POST':
        form = EditSkill(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = EditSkill(instance=skill)

    return render(request, 'edit_skill.html', {'form': form, 'skill': skill,'user_profile':user_profile})

def delete_skill(request,skill_id):
    skill = get_object_or_404(Skill, pk=skill_id)
    skill.delete()
    return redirect('show_skills')

def all_messages(request):
    user_profile = request.user.userprofile
    messages = ContactMessage.objects.all()
    return render(request, 'messages.html',{'messages':messages,'user_profile':user_profile})

def delete_message(request,message_id):
    blog = get_object_or_404(ContactMessage, id=message_id)
    blog.delete()
    return redirect('messages')


def upload_resume(request):
    user_profile = request.user.userprofile
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)

        if form.is_valid():
            existing_resume = Resume.objects.first()
            if existing_resume:
                existing_resume.file.delete()
                existing_resume.delete()

            form.save()
            return redirect('dashboard')
    else:
        form = ResumeForm()

    return render(request, 'resume_upload.html', {'form': form, 'user_profile':user_profile})