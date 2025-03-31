- **Pasos para crear el entorno virtual**:
    - Remove-Item -Recurse -Force .venv
    - python -m venv .venv
    - .venv\Scripts\activate
        - tiene que estar activo siempre para que funcione
    - pip install django
    - django-admin startproject proyecto .
    - python manage.py migrate
        - crea la base de datos
    - python manage.py runserver
        - levanta el servidor


