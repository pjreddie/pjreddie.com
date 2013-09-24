
from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify

class File(models.Model):
    upload = models.FileField(upload_to="files")
    def __unicode__(self):
        return self.upload.url
