from django.contrib import admin

from apps.common import models


@admin.register(models.VersionHistory)
class VersionHistoryAdmin(admin.ModelAdmin):
    list_display = ("version", "required", "created_at", "updated_at")
    list_filter = ("required", "created_at", "updated_at")
    search_fields = ("version",)
