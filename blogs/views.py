from django.shortcuts import render,redirect,get_object_or_404
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

def edit_blog(request, blog_id):
    blog = get_object_or_404(Blogs, id=blog_id)

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('show_blogs')
    else:
        form = BlogForm(instance=blog)

    return render(request, 'edit_blog.html', {'form': form, 'blog': blog})

def delete_blog(request,blog_id):
    blog = get_object_or_404(Blogs, id=blog_id)
    blog.delete()
    return redirect('show_blogs')