from django.urls import path
from .views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TasksDeleteView,
    TagsListView,
    TagsCreateView,
    TagsUpdateView,
    TagsDeleteView,
    progress_changing
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete", TasksDeleteView.as_view(), name="task-delete"),
    path("tasks/<int:pk>/change_progress", progress_changing, name="change-progress"),
    path("tags/", TagsListView.as_view(), name="tags-list"),
    path("tags/create/", TagsCreateView.as_view(), name="tags-create"),
    path("tags/<int:pk>/update", TagsUpdateView.as_view(), name="tags-update"),
    path("tags/<int:pk>/delete", TagsDeleteView.as_view(), name="tags-delete"),
]

app_name = "todo"
