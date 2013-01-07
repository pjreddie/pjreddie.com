from django.contrib import admin
from pjreddie.core.models import Image, Project, File

admin.site.register(Image)
admin.site.register(File)
admin.site.register(Project)
