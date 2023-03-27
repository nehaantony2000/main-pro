from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from Account.models import Account
from Company.models import JobDetails
from Employee.models import Applylist
from django.contrib.auth.models import Group
from django.contrib.admin.models import LogEntry



class UserAdmin(admin.ModelAdmin):
    list_display = ['jobname', 'companyname','companyaddress']

admin.site.register(JobDetails,UserAdmin)

