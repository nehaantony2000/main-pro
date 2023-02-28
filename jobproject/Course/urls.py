from django.urls import path
from . import views


urlpatterns = [

    path ('course-all/', views.course, name="courses"),
    path ('singlecourse/<int:id>/', views.singlecourse, name="singlecourse"),
]