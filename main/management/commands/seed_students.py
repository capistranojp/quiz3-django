from django.core.management.base import BaseCommand
from main.models import Student

SAMPLES = [
    ('2024-00101', 'Isabella Navarro', 'BS Computer Science', 2, 'A', 'Scholar'),
    ('2024-00102', 'Miguel Villanueva', 'BS Information Technology', 3, 'B', 'Regular'),
    ('2024-00103', 'Sofia Bautista', 'BS Computer Engineering', 1, 'C', 'Regular'),
    ('2024-00104', 'Gabriel Ramos', 'BS Information Systems', 4, 'A', 'Irregular'),
    ('2024-00105', 'Camille Aquino', 'BS Computer Science', 3, 'B', 'Scholar'),
]


class Command(BaseCommand):
    help = 'Adds sample student records (safe to run more than once).'

    def handle(self, *args, **kwargs):
        for num, name, program, year, section, status in SAMPLES:
            _, created = Student.objects.get_or_create(
                student_number=num,
                defaults=dict(full_name=name, program=program, year_level=year,
                              section=section, status=status),
            )
            self.stdout.write(('Added ' if created else 'Exists ') + name)
