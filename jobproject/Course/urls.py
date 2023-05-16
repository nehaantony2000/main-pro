from django.urls import path
from . import views


urlpatterns = [
  

    path('coursesenrolled/', views.coursesenrolled, name='coursesenrolled'),
    path('availablecourses/', views.availablecourses, name='availablecourses'),

    path('endroll/<slug:c_slug>/', views.Course_endroll, name='endroll'),

     path('feedback/', views.feedback, name='feedback'),
    # path('addvideo/', views.AddVideo, name='addvideo'),
    path('course_cancel/<int:course_id>/', views.Course_cancel, name='course_cancel'),
    path('playcourse/<slug:c_slug>', views.playcourse, name='playcourse'),
    path('playcourse/<slug:c_slug>', views.playcourse, name='playcourse'),
    path('playcourse/<slug:c_slug>/<slug:v_slug>', views.playcourse, name='playcourse'),
    path('course/<slug:c_slug>/checkoutcourse/', views.checkoutcourse, name='checkoutcourse'),
    path('payment_done_course/', views.payment_done_course, name='payment_done_course'),
    path('feedback/<int:feedback_id>/sentiment_analysis/', views.sentiment_analysis, name='sentiment_analysis')

    
]