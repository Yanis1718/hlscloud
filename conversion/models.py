from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Project(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    project_title = models.CharField(max_length=200)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.project_title


class File(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    file = models.FileField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.file

    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)
