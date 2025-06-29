from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from .models import Task
from .forms import TaskForm
# List view – Display, filter, and paginate tasks
def task_list(request):
    query = request.GET.get("q", "")
    tasks = Task.objects.all().order_by("id")
    if query:
        tasks = tasks.filter(name_of_task__icontains=query)
    paginator = Paginator(tasks, 10)
    page_number = request.GET.get("page")
    try:
        tasks_page = paginator.get_page(page_number)
    except (PageNotAnInteger, EmptyPage):
        tasks_page = paginator.get_page(1)
    return render(request, "task/task_list.html", {
        "tasks": tasks_page,
        "query": query
    })
# Create & Update view – Handle task form submissions
def task_form(request, id=None):
    task = get_object_or_404(Task, id=id) if id else None
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task saved successfully.")
            return redirect("task_list")
    else:
        form = TaskForm(instance=task)
    return render(request, "task/task_form.html", {"form": form})
# Delete view – Remove a task entry
def task_delete(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    messages.warning(request, f"Task '{task.name_of_task}' deleted.")
    return redirect("task_list")

