from django.contrib import admin
from .models import Subject


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = (
        'subject_code',
        'subject_name',
    )

    search_fields = (
        'subject_code',
        'subject_name',
    )