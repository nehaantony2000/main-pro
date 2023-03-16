from django.urls import path
from . import views


urlpatterns = [

 path('res', views.res, name='res'),
 path('resdetails', views.resdetails, name='resdetails'),
  path('resubmit', views.resubmit, name='resubmit'),
    ]