from django.contrib import admin
from .models import Project, File, ConvertedFolder
# Register your models here.
admin.site.register(Project)
admin.site.register(File)
admin.site.register(ConvertedFolder)
