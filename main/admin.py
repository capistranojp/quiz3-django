from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_number', 'full_name', 'program', 'year_level', 'section', 'status')
    list_filter = ('program', 'year_level', 'status')
    search_fields = ('student_number', 'full_name')
