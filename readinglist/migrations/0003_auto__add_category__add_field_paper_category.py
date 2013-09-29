# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table('readinglist_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('readinglist', ['Category'])

        # Adding field 'Paper.category'
        db.add_column('readinglist_paper', 'category',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='papers', null=True, to=orm['readinglist.Category']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table('readinglist_category')

        # Deleting field 'Paper.category'
        db.delete_column('readinglist_paper', 'category_id')


    models = {
        'readinglist.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'readinglist.paper': {
            'Meta': {'object_name': 'Paper'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'papers'", 'null': 'True', 'to': "orm['readinglist.Category']"}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'pdf': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['readinglist']