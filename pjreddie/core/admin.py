from django.contrib import admin
from pjreddie.core.models import Image, Project, File

class ImageInline(admin.TabularInline):
    model = Image

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

admin.site.register(Image)
admin.site.register(File)
admin.site.register(Project, ProjectAdmin)
