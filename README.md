# 🎓 API Gestión Académica - Actividad 2.2

## ⚙️ Setup (hazlo una sola vez)

### 1. Instala Python si no lo tienes
Descarga Python 3.11+ desde https://python.org

### 2. Crea el entorno virtual
```bash
# Entra a la carpeta del proyecto
cd universidad

# Crea el venv
python -m venv venv

# Actívalo (Windows)
venv\Scripts\activate

# Actívalo (Mac/Linux)
source venv/bin/activate
```

### 3. Instala dependencias
```bash
pip install django djangorestframework
```

### 4. Aplica las migraciones (crea la BD)
```bash
python manage.py migrate
```

### 5. Pobla la BD con datos nuevos
```bash
python manage.py shell < poblar_datos.py
```

---

## ▶️ Correr el servidor

```bash
python manage.py runserver
```

Abre el browser en: **http://127.0.0.1:8000/api/**

---

## 🔗 Endpoints disponibles

| Método | URL | Descripción |
|--------|-----|-------------|
| GET/POST | `/api/students/` | Lista y crea estudiantes |
| GET/PUT/DELETE | `/api/students/{id}/` | Detalle de estudiante |
| GET | `/api/students/?name=jesus` | Buscar por nombre |
| GET | `/api/students/{id}/courses/` | Cursos de un estudiante |
| GET | `/api/students/average_above_90/` | Estudiantes con promedio > 90 |
| GET/POST | `/api/courses/` | Lista y crea cursos |
| GET | `/api/courses/{id}/students/` | Estudiantes de un curso |
| GET | `/api/courses/more_than_5_students/` | Cursos con +5 estudiantes |
| GET/POST | `/api/enrollments/` | Lista y crea inscripciones |

---

## 📬 Ejemplos para Postman

### Crear estudiante
```
POST http://127.0.0.1:8000/api/students/
Body (JSON):
{
    "name": "Nuevo Estudiante",
    "email": "nuevo@cesunbc.edu.mx",
    "enrollment_date": "2024-03-01"
}
```

### Crear inscripción
```
POST http://127.0.0.1:8000/api/enrollments/
Body (JSON):
{
    "student": 1,
    "course": 2,
    "enrollment_date": "2024-03-01",
    "final_grade": 85.5
}
```

### Buscar estudiante por nombre
```
GET http://127.0.0.1:8000/api/students/?name=jesus
```

### Estudiantes con promedio > 90
```
GET http://127.0.0.1:8000/api/students/average_above_90/
```

### Cursos con más de 5 estudiantes
```
GET http://127.0.0.1:8000/api/courses/more_than_5_students/
```
