# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'justTest.record'
        db.delete_column('anytable_v1_justtest', 'record')


    def backwards(self, orm):
        # Adding field 'justTest.record'
        db.add_column('anytable_v1_justtest', 'record',
                      self.gf('django.db.models.fields.CharField')(blank=True, max_length=255, default=''),
                      keep_default=False)


    models = {
        'anytable_v1.city': {
            'Meta': {'object_name': 'City'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anytable_v1.Region']"})
        },
        'anytable_v1.event': {
            'Meta': {'object_name': 'Event'},
            'QR': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'default': "''"}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'event_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'event_time': ('django.db.models.fields.TimeField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'venue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anytable_v1.Venue']"})
        },
        'anytable_v1.justtest': {
            'Meta': {'object_name': 'justTest'},
            'file': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'anytable_v1.region': {
            'Meta': {'object_name': 'Region'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'default': "''"})
        },
        'anytable_v1.subscriber': {
            'Meta': {'object_name': 'Subscriber'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logIn': ('django.db.models.fields.CharField', [], {'max_length': '255', 'default': "''"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'default': "''"}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '255', 'default': "''"})
        },
        'anytable_v1.testcities': {
            'Meta': {'object_name': 'TestCities'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'population': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'anytable_v1.testusers': {
            'Meta': {'object_name': 'TestUsers'},
            'firstName': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastName': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'anytable_v1.user': {
            'Meta': {'object_name': 'User'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anytable_v1.City']"}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.NullBooleanField', [], {'blank': 'True', 'null': 'True', 'default': 'False'}),
            'joined': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True', 'null': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'telephone': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'anytable_v1.venue': {
            'Meta': {'object_name': 'Venue'},
            'address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['anytable_v1.City']"}),
            'cropping': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255'}),
            'facebook_url': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'kitchen': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['anytable_v1.VenueKitchen']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'option': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'null': 'True', 'to': "orm['anytable_v1.VenueOptions']"}),
            'schedule': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255'}),
            'subscriber': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['anytable_v1.Subscriber']"}),
            'tel': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255'}),
            'type': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['anytable_v1.VenueType']"}),
            'vk_url': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'blank': 'True', 'null': 'True'}),
            'website': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255'})
        },
        'anytable_v1.venueadministrator': {
            'Meta': {'object_name': 'VenueAdministrator'},
            'active': ('django.db.models.fields.NullBooleanField', [], {'blank': 'True', 'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'venue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anytable_v1.Venue']"})
        },
        'anytable_v1.venueimage': {
            'Meta': {'object_name': 'Venueimage'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True', 'null': 'True'}),
            'venue': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['anytable_v1.Venue']"})
        },
        'anytable_v1.venuekitchen': {
            'Meta': {'object_name': 'VenueKitchen'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255'})
        },
        'anytable_v1.venueoptions': {
            'Meta': {'object_name': 'VenueOptions'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'anytable_v1.venuetype': {
            'Meta': {'object_name': 'VenueType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['anytable_v1']