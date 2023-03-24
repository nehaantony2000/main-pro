from django import forms

from Employee.models import Videos


class VideoForm(forms.ModelForm):
    class Meta:
      model=Videos
      fields=["title","video","course"]