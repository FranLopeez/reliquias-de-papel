# Reliquias de Papel

Blog literario desarrollado con Django, donde los usuarios pueden reseñar libros, comentar reseñas ajenas y gestionar su perfil.

## URL pública

🔗 https://reliquias-de-papel.onrender.com

> **Nota:** el proyecto está desplegado en el plan gratuito de Render, que "duerme" el servicio tras ~15 minutos de inactividad. La primera carga después de un período sin uso puede tardar entre 30 y 60 segundos.

## Funcionalidades

- **Panel de administración** (Django Admin) para gestionar libros, reseñas, comentarios, perfiles y mensajes de contacto.
- **Registro, login y logout** de usuarios, con validaciones de seguridad estándar de Django (contraseñas robustas, protección CSRF).
- **Perfiles de usuario**: cada cuenta tiene un perfil editable (bio, fecha de nacimiento, avatar), creado automáticamente al registrarse.
- **Catálogo de libros**: listado con búsqueda por título/autor y filtro por género, con paginación.
- **Reseñas**: los usuarios logueados pueden crear reseñas de libros con puntuación (1 a 5).
- **Comentarios**: cualquier persona (con o sin cuenta) puede comentar una reseña.
- **Formulario de contacto**: los mensajes quedan guardados y son visibles (solo lectura) desde el panel admin.

## Tecnologías

- Python 3.14
- Django 6.1
- PostgreSQL (producción) / SQLite (desarrollo local)
- WhiteNoise (archivos estáticos en producción)
- Gunicorn (servidor de producción)
- Desplegado en Render

## Cómo ejecutar el proyecto localmente

### Requisitos previos

- Python 3.14 o superior
- Git

### Pasos

1. Cloná el repositorio:
```bash
   git clone https://github.com/FranLopeez/reliquias-de-papel.git
   cd reliquias-de-papel
```

2. Creá y activá un entorno virtual:
```bash
   python -m venv .venv
   .venv\Scripts\Activate.ps1   # Windows PowerShell
```

3. Instalá las dependencias:
```bash
   pip install -r requirements.txt
```

4. Creá un archivo `.env` en la raíz del proyecto con el siguiente contenido:

SECRET_KEY=clave-secreta-de-ejemplo-cambiar-por-una-propia
DEBUG=True

5. Aplicá las migraciones:
```bash
   python manage.py migrate
```

6. (Opcional) Cargá los libros de ejemplo:
```bash
   python manage.py load_books
```

7. Creá un superusuario para acceder al panel admin:
```bash
   python manage.py createsuperuser
```

8. Levantá el servidor:
```bash
   python manage.py runserver
```

9. Abrí `http://127.0.0.1:8000/` en el navegador.

## Estructura del proyecto

Reliquias_de_Papel/
├── books/ # Libros, listado, búsqueda, filtros, contacto
├── reviews/ # Reseñas y comentarios
├── users/ # Registro, login, perfiles
├── templates/ # Templates compartidos (base.html)
├── build.sh # Script de build para Render
├── requirements.txt
└── manage.py


## Autor

Pedro F López