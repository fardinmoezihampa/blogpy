from django.contrib import admin
from .models import *


class AdminUserProfile(admin.ModelAdmin):
    list_display = ['user']


class AdminCategory(admin.ModelAdmin):
    list_display = ['title']


class AdminArticle(admin.ModelAdmin):
    list_display = ['title', 'category', 'author']
    list_filter = ['category', 'author']
    search_fields = ['category', 'author']


admin.site.register(UserProFile, AdminUserProfile)
admin.site.register(Category, AdminCategory)
admin.site.register(Article, AdminArticle)
