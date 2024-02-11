from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest

from todos.forms import TodoForm
from .models import Todo

def task_lists(request):
    todos = Todo.objects.all()
    return render(request, 'index.html', {'todo_list': todos})

def add_task(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_lists')  # Redirect to the task list page after saving
    else:
        form = TodoForm()
    return render(request, 'index.html', {'form': form})
    
def delete_task(request, todo_id):
    Todo.objects.filter(id=todo_id).delete()
    return redirect('/list/')

def update_task(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == 'POST':
        todo.task = request.POST.get('task')
        todo.description = request.POST.get('description', '')
        todo.due_date = request.POST.get('due_date', None)
        todo.priority = request.POST.get('priority', None)
        todo.save()
        return redirect('/list/')
    else:
        return render(request, 'update_task.html', {'todo': todo})
