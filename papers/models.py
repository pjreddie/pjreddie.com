from django.db import models
from pjreddie.utils import markdown_to_html
from django.template.defaultfilters import slugify

class Paper( models.Model ):
    title = models.CharField( max_length=200 )
    abstract = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    authors = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    arxiv = models.URLField(max_length=1000, null=True, blank=True)
    slides = models.URLField(max_length=1000, null=True, blank=True)
    talk = models.URLField(max_length=1000, null=True, blank=True)
    link = models.URLField(max_length=1000, null=True, blank=True)
    pdf = models.FileField(upload_to="files/papers", null=True, blank=True)
    reviews = models.TextField(null=True, blank=True)
    slug = models.SlugField(blank=True, null=True)
    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Paper, self).save(*args, **kwargs)

    def html(self):
        return markdown_to_html( self.reviews, [] )

# Create your models here.
