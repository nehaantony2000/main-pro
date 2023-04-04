from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from Account.models import Account
from Company.models import JobDetails,Applicants
from Employee.models import Applylist
from django.contrib.auth.models import Group
from django.contrib.admin.models import LogEntry



class UserAdmin(admin.ModelAdmin):
    list_display = ['email','jobname', 'companyname','companyaddress','date_posted']
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
        
        return super().render_change_form(request, context, add, change, form_url, obj)
    def has_add_permission(self, request):
          return False
    def has_change_permission(self, request):
          return False    
admin.site.register(JobDetails,UserAdmin)

class UserAdmin(admin.ModelAdmin):
     list_display = ['applicant', 'job','date_posted']
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
        return super().render_change_form(request, context, add, change, form_url, obj)
     def has_add_permission(self, request):
          return False
     def has_change_permission(self, request):
          return False 
admin.site.register(Applicants,UserAdmin)