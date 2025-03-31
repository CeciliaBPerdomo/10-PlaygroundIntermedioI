# Family > views.py
from django.shortcuts import render, get_object_or_404
from .models import Familia

# Create your views here.
def lista_familia(request):
    familias = Familia.objects.all()
    return render(request, 'Family/lista_familia.html', {'familia': familias})