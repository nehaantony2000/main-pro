
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account
from django.contrib.auth.models import Group
from django.contrib.admin.models import LogEntry

LogEntry.objects.all().delete()


admin.site.unregister(Group)
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['username' ,'email','contact']
    # def has_add_permission(self, request):
    #     return False
    # def has_change_permission(self, request):
    #     return False 
    # def has_delete_permission(self, request, obj=None):
    #     return request.user.is_superuser
    # def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
    #     context.update({
    #         'show_save': False,
    #         'show_save_and_continue': False,
    #         'show_save_and_add_another': False,
    #         'show_delete': False,
    #         'Groups': False
    #     })
        
    #     return super().render_change_form(request, context, add, change, form_url, obj)

admin.site.register(Account, UserAdmin)

