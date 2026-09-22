from django.contrib import admin
from .models import Exam, Result


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = (
        'exam_name',
        'academic_year',
    )

    search_fields = (
        'exam_name',
        'academic_year',
    )


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = (
        'student',
        'subject',
        'exam',
        'marks',
        'max_marks',
        'grade',
    )

    list_filter = (
        'exam',
        'subject',
        'grade',
    )

    search_fields = (
        'student__full_name',
        'student__roll_number',
        'subject__subject_name',
    )