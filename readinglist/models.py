from django.db import models

class Paper( models.Model ):
    title = models.CharField( max_length=200 )
    description = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=1000, null=True, blank=True)
    pdf = models.FileField(upload_to="files/papers", null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.title
