from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User, Category, Article


@admin.register(User)
class UserAdmin(BaseUserAdmin):

    list_display = (
        'username',
        'email',
        'is_staff',
        'is_active'
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'created_at'
    )

    search_fields = ('name',)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'owner',
        'published',
        'created_at'
    )

    list_filter = (
        'published',
        'categories'
    )

    search_fields = (
        'title',
        'description'
    )

    filter_horizontal = ('categories',)
