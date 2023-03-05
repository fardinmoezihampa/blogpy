from django.contrib import admin
from .models import *


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user','avatar']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','avatar']


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'author','created_at']
    list_filter = ['category', 'author']
    search_fields = ['title', 'category', 'author']


admin.site.register(UserProFile, UserProfileAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
