# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Image'
        db.delete_table('core_image')

        # Deleting model 'Project'
        db.delete_table('core_project')


    def backwards(self, orm):
        # Adding model 'Image'
        db.create_table('core_image', (
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(related_name='images', null=True, to=orm['core.Project'], blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('core', ['Image'])

        # Adding model 'Project'
        db.create_table('core_project', (
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('start', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('kind', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('end', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal('core', ['Project'])


    models = {
        'core.file': {
            'Meta': {'object_name': 'File'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'upload': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['core']