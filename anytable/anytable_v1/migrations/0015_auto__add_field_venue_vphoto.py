# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'venue.vphoto'
        db.add_column('anytable_v1_venue', 'vphoto',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anytable_v1.photo'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'venue.vphoto'
        db.delete_column('anytable_v1_venue', 'vphoto_id')


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
            'image': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'photo': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['anytable_v1.photo']", 'blank': 'True', 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'venue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anytable_v1.venue']"})
        },
        'anytable_v1.photo': {
            'Meta': {'object_name': 'photo'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'})
        },
        'anytable_v1.region': {
            'Meta': {'object_name': 'region'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'default': "''"})
        },
        'anytable_v1.subscriber': {
            'Meta': {'object_name': 'subscriber'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logIn': ('django.db.models.fields.CharField', [], {'max_length': '255', 'default': "''"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'default': "''"}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '255', 'default': "''"})
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
            'email': ('django.db.models.fields.EmailField', [], {'db_index': 'True', 'max_length': '75', 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'joined': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True', 'null': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True'})
        },
        'anytable_v1.venue': {
            'Meta': {'object_name': 'venue'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anytable_v1.city']", 'null': 'True'}),
            'cropping': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'schedule': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255'}),
            'subscriber': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anytable_v1.subscriber']", 'null': 'True'}),
            'tel': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anytable_v1.venueType']", 'null': 'True'}),
            'vphoto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anytable_v1.photo']", 'null': 'True'})
        },
        'anytable_v1.venuetype': {
            'Meta': {'object_name': 'venueType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['anytable_v1']