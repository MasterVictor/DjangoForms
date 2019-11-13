from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import Profile
from django.contrib.auth.models import User
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display=('user','descripcion','telefono','picture')


class ProfileInLine(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'


class UserAdmin(BaseUserAdmin):
    inlines= (ProfileInLine,)

admin.site.unregister(User)
admin.site.register(User,UserAdmin)