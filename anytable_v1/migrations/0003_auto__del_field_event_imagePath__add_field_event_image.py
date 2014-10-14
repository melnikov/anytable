# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'event.imagePath'
        db.delete_column('anytable_v1_event', 'imagePath')

        # Adding field 'event.image'
        db.add_column('anytable_v1_event', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'event.imagePath'
        db.add_column('anytable_v1_event', 'imagePath',
                      self.gf('django.db.models.fields.CharField')(max_length=1024, default=''),
                      keep_default=False)

        # Deleting field 'event.image'
        db.delete_column('anytable_v1_event', 'image')


    models = {
        'anytable_v1.city': {
            'Meta': {'object_name': 'city'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anytable_v1.region']"})
        },
        'anytable_v1.event': {
            'Meta': {'object_name': 'event'},
            'QR': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'default': "''"}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'venue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anytable_v1.venue']"})
        },
        'anytable_v1.region': {
            'Meta': {'object_name': 'region'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'default': "''"})
        },
        'anytable_v1.testcities': {
            'Meta': {'object_name': 'testCities'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'population': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'anytable_v1.testusers': {
            'Meta': {'object_name': 'testUsers'},
            'firstName': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastName': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'anytable_v1.venue': {
            'Meta': {'object_name': 'venue'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['anytable_v1']