from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Task
from .forms import TaskForm
from .serializers import TaskSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
# Create your views here.


@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'todoApp/task_list.html',{"task_list":tasks})

@login_required
def task_detail(request,pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    return render(request,'todoApp/task_detail.html',{'task':task})

@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'todoApp/task_create.html',{'form':form})


@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)  # pk로 Task 객체를 가져옴
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_detail', pk=task.pk)  # pk가 제대로 전달되어야 함
    else:
        form = TaskForm(instance=task)
    return render(request, 'todoApp/task_update.html', {'form': form, 'task': task})


@login_required
def task_delete(request,pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'todoApp/task_delete.html',{'task':task})

@login_required
def task_complete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.completed = True
    task.save()
    return redirect('task_list')

@login_required
def task_toggle(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')

@login_required
def toggle_complete(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id)
        task.completed = not task.completed
        task.save()
        return redirect('task_list')



# API
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save()