from django.shortcuts import render,get_object_or_404,redirect
from .models import PortfolioProject, ProjectReview
from .forms import ProjectForm,ReviewForm

from django.db.models import Avg
# Create your views here.

def portfolio_project(request):
    projects_with_avg_ratings = PortfolioProject.objects.annotate(avg_rating=Avg('projectreview__ratings'))
    projects_sorted_by_rating = projects_with_avg_ratings.order_by('-avg_rating')
    return render(request, 'projects.html', {'projects': projects_sorted_by_rating})


def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  
            return redirect('projects')
    else:
        form = ProjectForm()
    return render(request, 'add_project.html', {'form': form})

def portfolio_project_details(request,project_id):
    project = get_object_or_404(PortfolioProject, pk = project_id)
    reviews = ProjectReview.objects.filter(project=project)
    return render(request, 'details.html', {'project':project, 'reviews':reviews})

def create_review(request, project_id):
    project = get_object_or_404(PortfolioProject, pk = project_id)
    if request.method == 'GET':
        return render(request, 'reviewform.html', {'form':ReviewForm(), 'project':project})
    else:
        try:
            form = ReviewForm(request.POST)
            newreview = form.save(commit=False)
            newreview.project = project
            newreview.save()
            return redirect('details',newreview.project.id)
        except ValueError:
            return render(request, 'reviewform.html',{'form':ReviewForm(), 'project':project, 'error' : 'Bad Data'})


