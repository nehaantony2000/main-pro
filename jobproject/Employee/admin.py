from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from Employee.models import Applylist,Courses
from django.contrib.auth.models import Group
from django.contrib.admin.models import LogEntry



# Register your models here.




class UserAdmin(admin.ModelAdmin):
     list_display = ['cand','job','maxsalary', 'education','minsalary']
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
admin.site.register(Applylist,UserAdmin)


class CourseAdmin(admin.ModelAdmin):
    list_display = ('course','duration','amount','slug','desc')
    list_per_page = 10
    list_editable = ('duration','amount')
    prepopulated_fields = {'slug':('course',)}
admin.site.register(Courses,CourseAdmin)
