from django.urls import path
from . import views


urlpatterns = [
  

    path('coursesenrolled/', views.coursesenrolled, name='coursesenrolled'),
    path('availablecourses/', views.availablecourses, name='availablecourses'),

    path('endroll/<slug:c_slug>/', views.Course_endroll, name='endroll'),

     path('feedback/', views.feedback, name='feedback'),
    # path('addvideo/', views.AddVideo, name='addvideo'),
    path('course_cancel/<int:course_id>/', views.Course_cancel, name='course_cancel'),
    path('playcourse/', views.playcourse, name='playcourse'),
    path('playcourse/<slug:c_slug>', views.playcourse, name='playcourse'),
    path('playcourse/<slug:c_slug>/<slug:v_slug>', views.playcourse, name='playcourse'),


    
]