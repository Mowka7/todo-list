from django.shortcuts import render
from django.views import generic

from todo.models import Task, Tags


class TaskListView(generic.ListView):
    model = Task


class TagsListView(generic.ListView):
    model = Tags
