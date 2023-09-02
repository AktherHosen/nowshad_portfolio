from django import forms
from django.forms import Textarea
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class': 'form-control mb-2'})
        self.fields['email'].widget.attrs.update({'class': 'form-control mb-2'})
        self.fields['message'].widget.attrs.update({'class': 'form-control mb-2'})
        
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'email': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'message': Textarea(attrs={'rows': 4, 'class': 'form-control'}),
        }
        labels = {
                'name' : ('Enter your name'),
                'email' : ('Enter your email'),
                'message' : ('Enter your message')
            }