from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = (
        'file',
        'creator',
        'create_at',
        'updated_at',
    )
    list_display_links = (
        'file',
        'creator',
    )

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = (
        'image',
        'message',
        'creator',
        'create_at',
        'updated_at'
    )

@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = (
        'image',
        'creator',
        'create_at',
        'updated_at',
    )
