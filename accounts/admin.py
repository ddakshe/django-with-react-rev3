from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'created_at', 'updated_at']
    list_display_links = ['username']
    search_fields = ['username']
    list_filter = ['created_at', 'updated_at']
    list_per_page = 10
