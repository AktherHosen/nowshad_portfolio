from django.shortcuts import render
from projects.models import PortfolioProject
from account.models import UserProfile, Skill
from django.db.models import Avg
# Create your views here.
def home(request):
    skills = Skill.objects.all()
    projects_with_avg_ratings = PortfolioProject.objects.annotate(avg_rating=Avg('projectreview__ratings'))
    projects_sorted_by_rating = projects_with_avg_ratings.order_by('-avg_rating')
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'home.html', {'projects':projects_sorted_by_rating, 'user_profile' : user_profile, 'skills':skills})