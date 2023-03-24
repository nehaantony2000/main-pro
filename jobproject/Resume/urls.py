from django.urls import path
from . import views


urlpatterns = [

 path('res', views.res, name='res'),
 path('my_view', views.my_view, name='my_view'),
 path('resdetails', views.resdetails, name='resdetails'),
  path('resubmit', views.resubmit, name='resubmit'),
    ]