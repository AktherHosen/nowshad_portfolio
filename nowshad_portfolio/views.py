from django.shortcuts import render
from projects.models import PortfolioProject
# Create your views here.
def home(request):
    projects = PortfolioProject.objects.all()
    return render(request, 'home.html', {'projects':projects})