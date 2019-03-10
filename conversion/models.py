from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Project(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    project_title = models.CharField(max_length=200)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.project_title


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<usernmae>/<filename>
    return 'user_{0}/{1}/{2}'.format(instance.author.username, instance.project.project_title, filename)


class File(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to=user_directory_path)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.file

    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)


def user_converted_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<usernmae>/<filename>
    return 'user_{0}/{1}/{2}'.format(instance.author.username, instance.project.project_title, filename)


class ConvertedFolder(models.Model):
    folder = models.FileField(upload_to=user_converted_directory_path)
