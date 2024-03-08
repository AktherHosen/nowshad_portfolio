from django.shortcuts import render,get_object_or_404,redirect
from .models import PortfolioProject, ProjectReview
from .forms import ProjectForm,ReviewForm,EditProject


from django.db.models import Avg
# Create your views here.
def dashboard_project(request):
    projects = PortfolioProject.objects.all()
    user_profile = request.user.userprofile
    return render(request, 'dashboard_project.html',{'projects':projects, 'user_profile':user_profile})

from django.shortcuts import render
from django.db.models import Avg
from .models import PortfolioProject, ProjectReview

def portfolio_project(request):
    projects_with_avg_ratings = PortfolioProject.objects.annotate(avg_rating=Avg('projectreview__ratings'))
    projects_sorted_by_rating = projects_with_avg_ratings.order_by('-avg_rating')

    for project in projects_sorted_by_rating:
        avg_rating = project.avg_rating
        if avg_rating is not None:
            filled_stars = int(round(avg_rating))
            remainder = avg_rating - filled_stars
            half_star = remainder >= 0.5
            empty_stars = 5 - filled_stars - half_star
            project.stars_html = '<i class="fas fa-star"></i>' * filled_stars
            if half_star:
                project.stars_html += '<i class="fas fa-star-half-alt"></i>'
            project.stars_html += '<i class="far fa-star"></i>' * empty_stars
        else:
            project.stars_html = ""

    return render(request, 'projects.html', {'projects': projects_sorted_by_rating})


def portfolio_project_details(request, project_id):
    project = get_object_or_404(PortfolioProject, pk=project_id)
    reviews = ProjectReview.objects.filter(project=project)

    for review in reviews:
        filled_stars = review.ratings
        empty_stars = 7 - filled_stars

        # Construct HTML for star icons
        review.stars_html = '<i class="fas fa-star"></i>' * filled_stars
        review.stars_html += '<i class="far fa-star"></i>' * empty_stars

    context = {
        'project': project,
        'reviews': reviews,
    }

    return render(request, 'details.html', context)

def add_project(request):
    user_profile = request.user.userprofile
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  
            return redirect('projects')
    else:
        form = ProjectForm()
    return render(request, 'add_project.html', {'form': form , 'user_profile':user_profile})

def edit_project(request, project_id):
    project = get_object_or_404(PortfolioProject, id=project_id)
    user_profile = request.user.userprofile

    if request.method == 'POST':
        form = EditProject(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    else:
        form = EditProject(instance=project)

    return render(request, 'edit_project.html', {'form': form, 'project': project ,'user_profile':user_profile})

def delete_project(request,project_id):
    project = get_object_or_404(PortfolioProject, id=project_id)
    project.delete()
    return redirect('projects')

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


def delete_review(request,review_id):
    review = get_object_or_404(ProjectReview, pk=review_id)
    review.delete()
    return redirect('projects')

    