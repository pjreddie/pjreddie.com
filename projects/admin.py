from django.contrib import admin
from projects.models import Image, Project

class ImageInline(admin.TabularInline):
    model = Image

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

admin.site.register(Image)
admin.site.register(Project, ProjectAdmin)
