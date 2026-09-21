from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from classes.models import Class


class Student(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    roll_number = models.CharField(
        max_length=20,
        unique=True
    )

    full_name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    date_of_birth = models.DateField(
        null=True,
        blank=True
    )

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )

    phone = models.CharField(
        max_length=15,
        blank=True
    )

    address = models.TextField(
        blank=True
    )

    student_class = models.ForeignKey(
        Class,
        on_delete=models.SET_NULL,
        null=True,
        related_name='students'
    )

    def __str__(self):
        return f"{self.roll_number} - {self.full_name}"