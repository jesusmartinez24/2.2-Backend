import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'universidad.settings')
django.setup()

from api.models import Student, Course, Enrollment
from datetime import date

Enrollment.objects.all().delete()
Student.objects.all().delete()
Course.objects.all().delete()
print("Base de datos limpiada ✓")

estudiantes_data = [
    {"name": "Alice Johnson",    "email": "alice.johnson@university.edu",    "enrollment_date": date(2023, 1, 15)},
    {"name": "Bob Smith",        "email": "bob.smith@university.edu",        "enrollment_date": date(2023, 1, 15)},
    {"name": "Carol White",      "email": "carol.white@university.edu",      "enrollment_date": date(2023, 2, 10)},
    {"name": "David Brown",      "email": "david.brown@university.edu",      "enrollment_date": date(2023, 2, 20)},
    {"name": "Emma Davis",       "email": "emma.davis@university.edu",       "enrollment_date": date(2023, 3, 5)},
    {"name": "Frank Miller",     "email": "frank.miller@university.edu",     "enrollment_date": date(2023, 3, 12)},
    {"name": "Grace Wilson",     "email": "grace.wilson@university.edu",     "enrollment_date": date(2023, 4, 1)},
    {"name": "Henry Moore",      "email": "henry.moore@university.edu",      "enrollment_date": date(2023, 4, 18)},
    {"name": "Isla Taylor",      "email": "isla.taylor@university.edu",      "enrollment_date": date(2023, 5, 7)},
    {"name": "Jack Anderson",    "email": "jack.anderson@university.edu",    "enrollment_date": date(2023, 5, 22)},
]

estudiantes = []
for data in estudiantes_data:
    s = Student.objects.create(**data)
    estudiantes.append(s)
    print(f"  Estudiante: {s.name}")

cursos_data = [
    {"name": "Mobile Development",      "credits": 6, "professor": "Dr. Roberts"},
    {"name": "Database Systems",        "credits": 5, "professor": "Prof. Chen"},
    {"name": "Web Development",         "credits": 6, "professor": "Dr. Patel"},
    {"name": "Networks",                "credits": 4, "professor": "Prof. Garcia"},
    {"name": "Software Engineering",    "credits": 5, "professor": "Dr. Kim"},
]

cursos = []
for data in cursos_data:
    c = Course.objects.create(**data)
    cursos.append(c)
    print(f"  Curso: {c.name}")

inscripciones = [
    (estudiantes[0], cursos[0], date(2024, 1, 20), 91.5),
    (estudiantes[1], cursos[0], date(2024, 1, 20), 78.0),
    (estudiantes[2], cursos[0], date(2024, 1, 21), 95.0),
    (estudiantes[3], cursos[0], date(2024, 1, 21), 88.5),
    (estudiantes[4], cursos[0], date(2024, 1, 22), 72.0),
    (estudiantes[5], cursos[0], date(2024, 1, 22), 96.0),
    (estudiantes[6], cursos[0], date(2024, 1, 23), 84.0),

    (estudiantes[0], cursos[1], date(2024, 1, 20), 93.0),
    (estudiantes[2], cursos[1], date(2024, 1, 21), 68.5),
    (estudiantes[4], cursos[1], date(2024, 1, 22), 91.0),
    (estudiantes[6], cursos[1], date(2024, 1, 23), 55.0),
    (estudiantes[7], cursos[1], date(2024, 1, 24), 97.0),
    (estudiantes[8], cursos[1], date(2024, 1, 24), 83.0),

    (estudiantes[1], cursos[2], date(2024, 2, 5),  62.0),
    (estudiantes[3], cursos[2], date(2024, 2, 5),  89.0),
    (estudiantes[9], cursos[2], date(2024, 2, 6),  94.5),

    (estudiantes[5], cursos[3], date(2024, 2, 10), 77.0),
    (estudiantes[7], cursos[3], date(2024, 2, 10), 92.0),

    (estudiantes[8], cursos[4], date(2024, 2, 15), 86.0),
    (estudiantes[9], cursos[4], date(2024, 2, 15), 91.0),
]

for estudiante, curso, fecha, calif in inscripciones:
    e = Enrollment.objects.create(student=estudiante, course=curso, enrollment_date=fecha, final_grade=calif)
    print(f"  Inscripcion: {e.student.name} -> {e.course.name} ({e.final_grade})")

print(f"\n✅ LISTO! | Estudiantes: {Student.objects.count()} | Cursos: {Course.objects.count()} | Inscripciones: {Enrollment.objects.count()}")