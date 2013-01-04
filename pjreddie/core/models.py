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

class Project( models.Model ):
	title = models.CharField( max_length=100 )
	description = models.TextField(null=True, blank=True)
	body = models.TextField()
	images = models.ManyToManyField( Image, blank=True )
	start = models.DateField(blank=True, null=True)
	end = models.DateField(blank=True, null=True)
	
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
			
				
	def html(self):
		return markdown_to_html( self.body, self.images.all() )

	def __unicode__( self ):
		return self.title
