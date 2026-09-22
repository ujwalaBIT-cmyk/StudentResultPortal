# Register your models here.
from django.contrib import admin
from .models import Class


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = (
        'class_name',
        'section',
        'academic_year',
    )

    search_fields = (
        'class_name',
        'section',
        'academic_year',
    )