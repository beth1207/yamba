from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'skills_required', 'location', 'expiry_date',  'budget', 'is_negotiable']
        labels = {
            'budget': 'Budget (UGX)',
            'is_negotiable': 'Is the budget negotiable?',
        }
