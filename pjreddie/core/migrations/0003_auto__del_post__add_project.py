# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Post'
        db.delete_table('core_post')

        # Removing M2M table for field images on 'Post'
        db.delete_table('core_post_images')

        # Adding model 'Project'
        db.create_table('core_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('body', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('core', ['Project'])

        # Adding M2M table for field images on 'Project'
        db.create_table('core_project_images', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm['core.project'], null=False)),
            ('image', models.ForeignKey(orm['core.image'], null=False))
        ))
        db.create_unique('core_project_images', ['project_id', 'image_id'])


    def backwards(self, orm):
        # Adding model 'Post'
        db.create_table('core_post', (
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('core', ['Post'])

        # Adding M2M table for field images on 'Post'
        db.create_table('core_post_images', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('post', models.ForeignKey(orm['core.post'], null=False)),
            ('image', models.ForeignKey(orm['core.image'], null=False))
        ))
        db.create_unique('core_post_images', ['post_id', 'image_id'])

        # Deleting model 'Project'
        db.delete_table('core_project')

        # Removing M2M table for field images on 'Project'
        db.delete_table('core_project_images')


    models = {
        'core.image': {
            'Meta': {'object_name': 'Image'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.project': {
            'Meta': {'object_name': 'Project'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['core.Image']", 'symmetrical': 'False', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['core']