from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Task1
# Create your views here.

def home(request):
    if request.method == 'POST':
        #adding Task
        if 'addTask' in request.POST:
            name = request.POST.get('name')
            description = request.POST.get('description')
            datetime = request.POST.get('datetime')
            time = request.POST.get('time')
            Task1.objects.create(name = name, descreption = description, datetime = datetime, time = time)
        
        #Deleting Task
        elif 'deleteTask' in request.POST:
            task_id = request.POST.get('Task_id')
            Task1.objects.filter(id = task_id).delete()
        return redirect('home')

    tasks = Task1.objects.all()
    return render(request, 'home.html', {'tasks': tasks})