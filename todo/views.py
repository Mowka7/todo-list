from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todo.forms import TaskForm
from todo.models import Task, Tags


class TaskListView(generic.ListView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:task-list")


class TasksDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:task-list")


def progress_changing(request, pk):
    task = Task.objects.get(pk=pk)
    task.progress = not task.progress
    task.save()
    return HttpResponseRedirect(reverse_lazy("todo:task-list"))


class TagsListView(generic.ListView):
    model = Tags


class TagsCreateView(generic.CreateView):
    model = Tags
    fields = "__all__"
    success_url = reverse_lazy("todo:tags-list")


class TagsUpdateView(generic.UpdateView):
    model = Tags
    fields = "__all__"
    success_url = reverse_lazy("todo:tags-list")


class TagsDeleteView(generic.DeleteView):
    model = Tags
    success_url = reverse_lazy("todo:tags-list")
