from django.shortcuts import render
from todo.models import ToDo
from todo.forms import ToDoForm

# Create your views here.


def home(request):
    return render(request, 'todo/home.html')


def todos(request):
    # do zrobienia
    current = ToDo.objects.filter(complete_date__isnull=True, user=request.user)
    #zakończone
    done = ToDo.objects.filter(complete_date__isnull=False, user=request.user)
    completed = done.count()
    return render(request, 'todo/todos.html', {'current': current, 'done': done, 'completed': completed})

# następnie  url+template + view do tworzenia zadań


