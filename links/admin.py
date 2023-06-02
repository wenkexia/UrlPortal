from django.contrib import admin

# Register your models here.

from . import models


@admin.register(models.Link)
class LinkModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'short_url', 'is_enabled', 'created_at', 'updated_at', 'user')
    list_filter = ('is_enabled',)
    search_fields = ('short',)


@admin.register(models.Url)
class UrlModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'original_url', 'description', 'created_at', 'updated_at', 'link')
    search_fields = ('original_url',)
