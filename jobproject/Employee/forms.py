from Company.models import JobAlert
from django import forms
class JobAlertForm(forms.ModelForm):
    class Meta:
        model = JobAlert
        fields = ['keywords', 'industry', 'experience_level', 'category', 'jobtype', 'location']
