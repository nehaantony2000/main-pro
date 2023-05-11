import textrazor
from django.conf import settings
from django.shortcuts import render
from .forms import JobPostingForm

# Initialize the TextRazor client
textrazor.api_key = settings.TEXTRAZOR_API_KEY
client = textrazor.TextRazor(extractors=["entities", "topics"])

def detect_fake_job_posting(request):
    if request.method == 'POST':
        # Get the job post text from the form
        form = JobPostingForm(request.POST)
        if form.is_valid():
            job_post_text = form.cleaned_data['text']
            
            # Analyze the job post text using TextRazor
            response = client.analyze(job_post_text)
            entities_with_dbpedia = []
            for entity in response.entities():
                if entity.id:
                    # Check for red flags in the response
                    for dbpedia_type in entity.dbpedia_types:
                        if dbpedia_type and 'Job' in dbpedia_type.label:
                            return render(request, 'fakejobpredictor/job_posting_form.html', {
                                'job_post_text': job_post_text,
                                'is_job_post_legitimate': False,
                                'form': form
                            })
                    entities_with_dbpedia.append(entity)
            
            # Render the appropriate template based on the prediction result and provide proof
            if not entities_with_dbpedia:
                return render(request, 'fakejobpredictor/job_posting_form.html', {
                    'job_post_text': job_post_text,
                    'is_job_post_legitimate': True,
                    'form': form
                })
            else:
                return render(request, 'fakejobpredictor/job_posting_form.html', {
                    'job_post_text': job_post_text,
                    'is_job_post_legitimate': False,
                    'form': form,
                    'entities_with_dbpedia': entities_with_dbpedia
                })
    else:
        form = JobPostingForm()
        return render(request, 'fakejobpredictor/job_posting_form.html', {'form': form})

