from django.forms import ModelForm,Textarea
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