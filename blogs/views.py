from django.shortcuts import render,redirect
from .models import Blogs
from . forms import BlogForm
# Create your views here.
def showblogs(request):
    blogs = Blogs.objects.all()
    return render(request, 'all_blogs.html', {'blogs':blogs})

def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  
            return redirect('show_blogs')
    else:
        form = BlogForm()
    return render(request, 'add_blogs.html', {'form': form})