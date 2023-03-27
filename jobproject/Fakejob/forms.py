# forms.py

from django import forms

class JobPostingForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
