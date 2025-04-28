from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.utils import timezone

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})

def task_update(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    return render(request, 'tasks/task_form.html', {'form': form})

def task_delete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('task_list')

def task_list(request):
    tasks = Task.objects.all()

    # Search logic
    query = request.GET.get('q')
    if query:
        tasks = tasks.filter(title__icontains=query)

    # Sort logic
    sort_by = request.GET.get('sort')
    if sort_by == 'high':
        tasks = tasks.order_by('-priority')
    elif sort_by == 'low':
        tasks = tasks.order_by('priority')

    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def task_list(request):
    tasks = Task.objects.all()

    # Search logic
    query = request.GET.get('q')
    if query:
        tasks = tasks.filter(title__icontains=query)

    # Sort logic
    sort_by = request.GET.get('sort')
    if sort_by == 'high':
        tasks = tasks.order_by('-priority')
    elif sort_by == 'low':
        tasks = tasks.order_by('priority')

    # Pagination logic
    paginator = Paginator(tasks, 5)  # Show 5 tasks per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'tasks/task_list.html', {'page_obj': page_obj})

def task_list(request):
    tasks = Task.objects.all()

    query = request.GET.get('q')
    if query:
        tasks = tasks.filter(title__icontains=query)

    sort_by = request.GET.get('sort')
    if sort_by == 'high':
        tasks = tasks.order_by('-priority')
    elif sort_by == 'low':
        tasks = tasks.order_by('priority')

    paginator = Paginator(tasks, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    today = timezone.now().date()

    return render(request, 'tasks/task_list.html', {'page_obj': page_obj, 'today': today})


# tasks/views.py

from django.shortcuts import get_object_or_404, redirect

def task_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = True
    task.save()
    return redirect('task_list')
