from django.shortcuts import render
from .models import Tarefas

def index(request):
    tarefas = Tarefas.objects.all()
    return render(request, 'index.html', {'tarefas':tarefas})

def adicionar(request):
    return render(request, 'adicionar.html')
