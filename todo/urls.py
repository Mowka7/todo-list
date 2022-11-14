from django.urls import path
from .views import (
    TaskListView,
    TagsListView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tags/", TagsListView.as_view(), name="tags-list")
]

app_name = "todo"
