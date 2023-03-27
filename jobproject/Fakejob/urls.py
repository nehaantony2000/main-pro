
# urls.py

from django.urls import path
from .views import detect_fake_job_posting

urlpatterns = [
    path('detect-fake-job-posting/', detect_fake_job_posting, name='detect_fake_job_posting'),
]
