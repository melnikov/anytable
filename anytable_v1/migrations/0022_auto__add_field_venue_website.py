# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'venue.website'
        db.add_column('anytable_v1_venue', 'website',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'venue.website'
        db.delete_column('anytable_v1_venue', 'website')


    models = {
        'anytable_v1.city': {
            'Meta': {'object_name': 'city'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anytable_v1.region']"})
        },
        'anytable_v1.event': {
            'Meta': {'object_name': 'event'},
            'QR': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1024'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'venue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anytable_v1.venue']"})
        },
        'anytable_v1.region': {
            'Meta': {'object_name': 'region'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'})
        },
        'anytable_v1.subscriber': {
            'Meta': {'object_name': 'subscriber'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logIn': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'password': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'})
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
        'anytable_v1.user': {
            'Meta': {'object_name': 'user'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anytable_v1.city']"}),
            'email': ('django.db.models.fields.EmailField', [], {'db_index': 'True', 'unique': 'True', 'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'joined': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'telephone': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'anytable_v1.venue': {
            'Meta': {'object_name': 'venue'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anytable_v1.city']", 'null': 'True'}),
            'cropping': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'schedule': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'subscriber': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anytable_v1.subscriber']", 'null': 'True'}),
            'tel': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anytable_v1.venueType']", 'null': 'True'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'anytable_v1.venueimage': {
            'Meta': {'object_name': 'venueimage'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'venue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anytable_v1.venue']", 'null': 'True'})
        },
        'anytable_v1.venuetype': {
            'Meta': {'object_name': 'venueType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['anytable_v1']