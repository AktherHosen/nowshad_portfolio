from django.forms import ModelForm,Textarea
from django import forms
from . models import Blogs
class BlogForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({'class': 'form-control mb-2'})
        self.fields['description'].widget.attrs.update({'class': 'form-control mb-2'})
        self.fields['blog_image'].widget.attrs.update({'class': 'form-control mb-2'})
        
    class Meta:
        model = Blogs
        fields = ['title', 'description', 'blog_image']
        widgets = {
            'description': Textarea(attrs={'rows': 4, 'class': 'form-control'}),
        }
        error_messages = {
            'blog_image': {
                'required': '',
            },
        }
        labels = {
                'title' : ('Write Blog Title'),
                'description' : ('Write Blog Description'),
                'blog_image' : ('Add Blog Image')
            }
class EditBlogForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ['title', 'description', 'blog_image']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'description': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'blog_image': forms.ClearableFileInput(attrs={'class': 'form-control mb-2'}),
        }
        labels = {
            'title': 'Edit Blog Title',
            'description': 'Edit Blog Description',
            'blog_image': 'Edit Blog Image',
        }