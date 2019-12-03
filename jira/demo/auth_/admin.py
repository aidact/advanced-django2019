from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# from .forms import CustomUserCreationForm, CustomUserChangeForm
from auth_.models import MainUser, Profile


@admin.register(MainUser)
class MainUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'is_staff', 'is_active',)
    # fields = (
    #     'username',
    #     'email',
    #     'first_name',
    #     'last_name',
    #     'date_joined',
    #     'is_staff',
    #     'is_active'
    # )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'address', 'bio')
    fields = (
        'user',
        'bio',
        'address'
    )
