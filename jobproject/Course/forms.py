from django import forms

from Employee.models import Videos


class VideoForm(forms.ModelForm):
    class Meta:
        model = Videos
        fields = ["title", "desp", "video", "course"]

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if len(title) < 30:
            raise forms.ValidationError("Title must be at least 30 characters long.")
        return title

    def clean(self):
        cleaned_data = super().clean()
        video = cleaned_data.get("video")
        if video and video.size > 10 * 1024 * 1024:
            raise forms.ValidationError("Video file size cannot exceed 10MB.")
        return cleaned_data