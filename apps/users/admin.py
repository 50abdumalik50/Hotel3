from django.contrib import admin

from apps.users.models import User


# from django.contrib.auth import get_user_model
#
# User = get_user_model()


# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ['username']
#     search_fields = ['username']

admin.site.register(User)