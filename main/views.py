from django.shortcuts import render
from .models import Student


def home(request):
    students = Student.objects.all()      # Model: fetch every student record
    context = {
        'students': students,             # View: send the data to the template
        'total': students.count(),
    }
    return render(request, 'main/home.html', context)
