from django.contrib import admin
from .models import User, Profile

# Register your models here.

@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'full_name', 'email', 'gender']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'verified']
    list_editable = ['verified']


# admin.site.register(User, CustomUserAdmin)
# admin.site.register(Profile, ProfileAdmin)