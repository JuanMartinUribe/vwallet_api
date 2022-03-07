from django.contrib import admin
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class MainUserInLine(admin.StackedInline):
    model = models.MainUser
    can_delete = False
    verbose_name_plural = 'Main Users'  

class CustomizedUserAdmin(UserAdmin):
    inlines = (MainUserInLine,)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name','id','status','quantity')

admin.site.unregister(User)
admin.site.register(User,CustomizedUserAdmin)
admin.site.register(models.Pocket)