# Family > urls.py
from django.urls import path
from .views import lista_familia

urlpatterns = [
    path('', lista_familia, name='lista_familia'),
]