from django.shortcuts import render,redirect
from .models import Task

def task_list(request):
    if request.method == 'POST':
        task_title = request.POST.get('title')
        if task_title:
            Task.objects.create(title=task_title)
        
        return redirect('task_list')
            
    tasks = Task.objects.all()
    return render(request, 'todo/task_list.html', {'tasks' : tasks})

