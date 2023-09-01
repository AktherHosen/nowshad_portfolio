from django import forms
from django.forms import Textarea
from .models import PortfolioProject,ProjectReview

class ProjectForm(forms.ModelForm):
    class Meta:
        model = PortfolioProject
        fields = ['title', 'description', 'technologies', 'project_url', 'screenshoot','category']
        

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