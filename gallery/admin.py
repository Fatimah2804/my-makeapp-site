from django.contrib import admin
from .models import GalleryLook, GalleryMedia


class GalleryMediaInline(admin.TabularInline):
    model = GalleryMedia
    extra = 1


@admin.register(GalleryLook)
class GalleryLookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at')
    list_filter = ('category',)
    inlines = [GalleryMediaInline]