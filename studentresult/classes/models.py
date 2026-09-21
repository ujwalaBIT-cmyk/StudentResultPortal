from django.db import models

# Create your models here.
class Class(models.Model):
    class_name = models.CharField(max_length=50)
    section = models.CharField(max_length=10)
    academic_year = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.class_name} - {self.section}"