from django.db import models
from students.models import Student
from subjects.models import Subject


class Exam(models.Model):
    exam_name = models.CharField(
        max_length=100
    )

    academic_year = models.CharField(
        max_length=20
    )

    def __str__(self):
        return f"{self.exam_name} - {self.academic_year}"


class Result(models.Model):

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='results'
    )

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name='results'
    )

    exam = models.ForeignKey(
        Exam,
        on_delete=models.CASCADE,
        related_name='results'
    )

    marks = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    max_marks = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=100
    )

    grade = models.CharField(
        max_length=5,
        blank=True
    )

    remarks = models.CharField(
        max_length=200,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return (
            f"{self.student.full_name} - "
            f"{self.subject.subject_name}"
        )