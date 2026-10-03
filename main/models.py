from django.db import models


class Student(models.Model):
    STATUS_CHOICES = [
        ('Regular', 'Regular'),
        ('Irregular', 'Irregular'),
        ('Scholar', 'Scholar'),
    ]

    student_number = models.CharField(max_length=15, unique=True)
    full_name = models.CharField(max_length=100)
    program = models.CharField(max_length=100)
    year_level = models.PositiveSmallIntegerField()
    section = models.CharField(max_length=10)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Regular')

    class Meta:
        ordering = ['student_number']

    def __str__(self):
        return f"{self.student_number} - {self.full_name}"
