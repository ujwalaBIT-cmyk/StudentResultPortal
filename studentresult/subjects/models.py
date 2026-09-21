from django.db import models

# Create your models here.
class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    subject_code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.subject_code} - {self.subject_name}"