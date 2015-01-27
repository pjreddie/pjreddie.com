from django.contrib import admin
from darknet.models import Post, Image

class ImageInline(admin.TabularInline):
    model = Image

class PostAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

admin.site.register(Image)
admin.site.register(Post, PostAdmin)
