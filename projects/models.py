from django.db import models

from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from pjreddie.utils import markdown_to_html

class Project( models.Model ):
    title = models.CharField( max_length=100 )
    description = models.TextField(null=True, blank=True)
    body = models.TextField()
    start = models.DateField(blank=True, null=True)
    end = models.DateField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    
    RESEARCH = 'R'
    SCHOOL = 'S'
    PERSONAL = 'P'
    PROJECT_KINDS = (
        (RESEARCH, 'Research'),
        (SCHOOL, 'School'),
        (PERSONAL, 'Personal'),
    )

    kind = models.CharField(max_length=2, choices=PROJECT_KINDS, null=True, blank=True)

    def formatted_date(self):
        start = self.start
        end = self.end
        if not start: return ''
        if start and not end:
            return start.strftime('%B %Y')
        elif start.year == end.year:
            if start.month == end.month:
                return start.strftime('%B %Y')
            else:
                return start.strftime('%B - ') + end.strftime('%B %Y')
        else:
            return start.strftime('%B %Y - ') + end.strftime('%B %Y')
                
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)

    def html(self):
        return markdown_to_html( self.body, self.images.all() )

    def __unicode__( self ):
        return self.title

class Image( models.Model ):
    name = models.CharField( max_length=100 )
    image = models.ImageField( upload_to="image" )
    project = models.ForeignKey(Project, blank=True, null=True, related_name = "images")

    def __unicode__( self ):
        return self.name
# Create your models here.
