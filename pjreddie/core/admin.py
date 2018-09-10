from django.contrib import admin
from pjreddie.core.models import File, Page, Image
from django.contrib import admin

admin.site.register(File)


class ImageInline(admin.TabularInline):
    model = Image

class PageAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

admin.site.register(Image)
admin.site.register(Page, PageAdmin)

