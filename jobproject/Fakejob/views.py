# views.py
from django.conf import settings
from .forms import JobPostingForm
from django.shortcuts import render
import textrazor

def detect_fake_job_posting(request):
    client = textrazor.TextRazor(extractors=["entities"])
    client.set_api_key(settings.TEXTRAZOR_API_KEY)
    if request.method == 'POST':
        text = request.POST.get('text', '')
        response = client.analyze(text)
        entities = [entity.id for entity in response.entities()]
        if 'fake' in entities:
            is_fake = True
        else:
            is_fake = False
        return render(request, 'Fakejobpredictor/results.html', {'text': text, 'is_fake': is_fake})
    else:
        form = JobPostingForm()
        return render(request, 'Fakejobpredictor/job_posting_form.html', {'form': form})
