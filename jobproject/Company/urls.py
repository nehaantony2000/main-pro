from django.urls import path
from . import views


urlpatterns = [


   path ('Companyhome/', views.Companyhome, name="Companyhome"),
    path ('postjob/', views.postjob, name="postjob"),
    path('postedjob/',views.postedjob, name="postedjob"),
    path('edit_jobdetails/<int:id>/',views.edit_jobdetails, name="edit_jobdetails"),
    path ('jobdetails/',views.JobdetailSubmit,name="jobdetails"),
    path ('profile/', views.profile, name="profile"),
    path ('Applylist/', views.JobApplylist, name="Applylist"),
    path('Applylist/<int:id>/update-status/', views.update_application_status, name='update_application_status'),
    path('job/<str:job_name>/applylist/', views.JobApplylist, name='job_applylist'),
    path ('viewjob/<int:id>', views.viewjob, name="viewjob"),
    path ('update_profile/', views.Update_profile, name="update_profile"),
    path('addvideo/', views.AddVideo, name='addvideo'),
    path('enrolledcandidate/', views.enrolledcandidate, name='enrolledcandidate'),
    path('job_delete/<int:id>', views.jobdelete, name='job_delete'),
    path('deleteApplication/<int:id>', views.deleteApplication, name='deleteApplication'),
    path('viewfeedback/', views.viewfeedback, name='viewfeedback'),
    path('note/<int:id>/',views.note, name='note'),
   
    path('list_selected_candidates/', views.list_selected_candidates, name='list_selected_candidates'),
    
    path('recruiter_videos/', views.recruiter_videos, name='recruiter_videos'),
    path('deletevedio/<int:id>', views.deletevedio, name='deletevedio'),
   path('edit_video/<int:id>/',views.edit_video, name='edit_video'),
   path('interview/<int:id>/', views.interview_schedule, name='interview_schedule'),
    path('Interview_App/', views.Interview_App, name='Interview_App'),




]