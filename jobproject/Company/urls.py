from django.urls import path
from . import views


urlpatterns = [


   path ('Companyhome/', views.Companyhome, name="Companyhome"),
    path ('postjob/', views.postjob, name="postjob"),
    path('postedjob/',views.postedjob, name="postedjob"),
    path ('jobdetails/',views.JobdetailSubmit,name="jobdetails"),
    path ('profile/', views.profile, name="profile"),
    path ('Applylist/', views.JobApplylist, name="Applylist"),
    path ('update_profile/', views.Update_profile, name="update_profile"),
    path('addvideo/', views.AddVideo, name='addvideo'),
    path('enrolledcandidate/', views.enrolledcandidate, name='enrolledcandidate'),
    path('job_delete/<int:id>', views.jobdelete, name='job_delete'),
    path('deleteApplication/<int:id>', views.deleteApplication, name='deleteApplication'),
    path('viewfeedback/', views.viewfeedback, name='viewfeedback'),
    
]