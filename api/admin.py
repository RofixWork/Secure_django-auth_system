from django.contrib import admin

from .models import Profile, User


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "email", "username", "is_superuser", "date_joined"]
    search_fields = ["email", "username"]
    list_filter = ["is_superuser", "date_joined"]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "user__full_name", "user__email"]
    search_fields = ["user__email", "user__username"]
    list_filter = ["user__is_superuser", "user__date_joined"]
