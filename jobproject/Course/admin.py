from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from matplotlib import path, pyplot as plt
from Employee.models import Courses,Course_purchase
from django.contrib.auth.models import Group
from django.contrib.admin.models import LogEntry
from django.http import HttpResponse
from io import BytesIO


class PurchaseManagement(admin.ModelAdmin):
    list_display = ("course","purhase_date","end_date")
    def has_add_permission(self, request):
        return False
    def has_change_permission(self, request):
        return False 
    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser
    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            'show_save': False,
            'show_save_and_continue': False,
            'show_save_and_add_another': False,
            'show_delete': False,
            'Groups': False
        })

admin.site.register(Course_purchase,PurchaseManagement)


class CourseAdmin(admin.ModelAdmin):
    list_display = ('course','duration','amount','slug','desc')
    list_per_page = 10
    list_editable = ('duration','amount')
    prepopulated_fields = {'slug':('course',)}
admin.site.register(Courses,CourseAdmin)


from django.contrib import admin
from django.http import HttpResponse
from io import BytesIO

from django.contrib import admin
from django.db.models import Avg
from django.http import HttpResponse
import matplotlib.pyplot as plt


  
   
