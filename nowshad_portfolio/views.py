from django.shortcuts import render
from projects.models import PortfolioProject
from account.models import UserProfile, Skill, Resume
from django.db.models import Avg
# Create your views here.
def home(request):
    skills = Skill.objects.all()
    resume = Resume.objects.first()
    projects_with_avg_ratings = PortfolioProject.objects.annotate(avg_rating=Avg('projectreview__ratings'))
    projects_sorted_by_rating = projects_with_avg_ratings.order_by('-avg_rating')

    if request.user.is_authenticated:
        try:
            user_profile = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            user_profile = None
        return render(request, 'home.html', {'projects': projects_sorted_by_rating, 'user_profile': user_profile, 'skills': skills, 'resume': resume})
    else:
        return render(request, 'home.html', {'projects': projects_sorted_by_rating, 'skills': skills, 'resume':resume})