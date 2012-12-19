import markdown

from django.db import models
from django.conf import settings

def markdown_to_html( markdownText, images ):    
    image_ref = ""

    for image in images:
        image_url = image.image.url
        image_ref = "%s\n[%s]: %s" % ( image_ref, image, image_url )

    md = "%s\n%s" % ( markdownText, image_ref )
    html = markdown.markdown( md )

    return html

class Image( models.Model ):
    name = models.CharField( max_length=100 )
    image = models.ImageField( upload_to="image" )

    def __unicode__( self ):
        return self.name

class Post( models.Model ):
    title = models.CharField( max_length=100 )
    body = models.TextField()
    images = models.ManyToManyField( Image, blank=True )

    def html( self ):
        return markdown_to_html( self.body, self.images.all() )
