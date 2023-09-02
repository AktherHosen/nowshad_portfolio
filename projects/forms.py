from django import forms
from django.forms import Textarea
from .models import PortfolioProject,ProjectReview

class ProjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({'class': 'form-control mb-2'})
        self.fields['description'].widget.attrs.update({'class': 'form-control mb-2'})
        self.fields['technologies'].widget.attrs.update({'class': 'form-control mb-2'})
        self.fields['project_url'].widget.attrs.update({'class': 'form-control mb-2'})
        self.fields['screenshoot'].widget.attrs.update({'class': 'form-control mb-2'})
        self.fields['category'].widget.attrs.update({'class': 'form-control mb-2'})
    
    class Meta:
        model = PortfolioProject
        fields = ['title', 'description', 'technologies', 'project_url', 'screenshoot', 'category']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'project_url': forms.URLInput(attrs={'class': 'form-control'}),
        }
        error_messages = {
            'screenshoot': {
                'required': '',
            },
        }
        labels = {
                'title' : ('Write Title'),
                'description' : ('Write Description'),
                'technologies' : ('Write Technologies'),
                'project_url' : ('Write Project_url'),
                'screenshoot' : ('Add Screenshoot'),
                'category' : ('Add Category'),   
            }
class EditProject(forms.ModelForm): 
    class Meta:
        model = PortfolioProject
        fields = ['title', 'description', 'technologies', 'project_url', 'screenshoot', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'description': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'technologies': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'project_url': forms.URLInput(attrs={'class': 'form-control'}),
            'screenshoot': forms.ClearableFileInput(attrs={'class': 'form-control mb-2'}),
            'category': forms.TextInput(attrs={'class': 'form-control mb-2'}),
        }
        labels = {
                'title' : ('Write Title'),
                'description' : ('Write Description'),
                'technologies' : ('Write Technologies'),
                'project_url' : ('Write Project_url'),
                'screenshoot' : ('Add Screenshoot'),
                'category' : ('Add Category'),   
            }
        
class ReviewForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args,**kwargs)
        self.fields['reviews'].widget.attrs.update({'class':'form-control'})
        self.fields['ratings'].widget.attrs.update({'class':'form-control'})
        
    class Meta:
            model = ProjectReview
            fields = ['reviews','ratings']
            widgets = {
            'reviews': Textarea(attrs={'row':4})
            }
            labels = {
                'reviews' : ('Write Review'),
                'ratings' : ('Give Rating'),
            }