from django.db import models
from django.contrib.auth.models import User


class Teacher(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    teacher_id = models.CharField(
        max_length=20,
        unique=True
    )

    full_name = models.CharField(
        max_length=100
    )

    email = models.EmailField(
        unique=True
    )

    phone = models.CharField(
        max_length=15,
        blank=True
    )

    department = models.CharField(
        max_length=100,
        blank=True
    )

    def __str__(self):
        return f"{self.teacher_id} - {self.full_name}"