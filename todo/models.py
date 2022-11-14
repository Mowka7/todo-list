from django.db import models


class Tags(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now_add=True)
    progress = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tags, related_name="tasks")

    class Meta:
        ordering = ["progress", "-datetime"]
