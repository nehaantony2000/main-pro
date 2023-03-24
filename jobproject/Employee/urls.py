from django.urls import path
from . import views


urlpatterns = [
    path('userhome/', views.userhome, name='userhome'),
   
    path ('category/', views.cat, name="category"),
    path ('Eprofile/', views.profile, name="Eprofile"),
    path ('Update_profile/', views.Update_profile, name="Update_profile"),
    path ('joblist/', views.joblist, name="joblist"),
    path('ApplyJob/<int:id>',views.ApplyJob, name="ApplyJob"),
    path ('Searchbar/', views.searchbar, name="searchbar"),
    path ('singlejob/<int:id>', views.singlejob, name="singlejob"),
    path('Apply/<int:pk>',views.Apply, name="Apply"),
    path('saved_job_list/', views.saved_jobs, name='saved-jobs'),
    path('save/<int:id>', views.save_job, name='save-job'),
  
  
 
]