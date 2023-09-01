from django.shortcuts import render,get_object_or_404,redirect
from .models import PortfolioProject, ProjectReview
from .forms import ProjectForm,ReviewForm
# Create your views here.
def portfolio_project(request):
    projects = PortfolioProject.objects.all()
    return render(request, 'projects.html',{'projects':projects})

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
        