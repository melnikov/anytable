# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PriceType'
        db.create_table('anytable_v1_pricetype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(null=True, max_length=255, blank=True)),
        ))
        db.send_create_signal('anytable_v1', ['PriceType'])

        # Adding model 'EventPrice'
        db.create_table('anytable_v1_eventprice', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('price_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anytable_v1.PriceType'])),
            ('price', self.gf('django.db.models.fields.CharField')(null=True, max_length=50, blank=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anytable_v1.Event'])),
        ))
        db.send_create_signal('anytable_v1', ['EventPrice'])

        # Deleting field 'Folder.password'
        db.delete_column('anytable_v1_folder', 'password')


        # Changing field 'Event.QR'
        db.alter_column('anytable_v1_event', 'QR', self.gf('django.db.models.fields.CharField')(null=True, max_length=1024))

    def backwards(self, orm):
        # Deleting model 'PriceType'
        db.delete_table('anytable_v1_pricetype')

        # Deleting model 'EventPrice'
        db.delete_table('anytable_v1_eventprice')

        # Adding field 'Folder.password'
        db.add_column('anytable_v1_folder', 'password',
                      self.gf('django.db.models.fields.CharField')(null=True, max_length=32),
                      keep_default=False)


        # Changing field 'Event.QR'
        db.alter_column('anytable_v1_event', 'QR', self.gf('django.db.models.fields.CharField')(max_length=1024))

    models = {
        'anytable_v1.city': {
            'Meta': {'object_name': 'City'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anytable_v1.Region']"})
        },
        'anytable_v1.document': {
            'Meta': {'object_name': 'Document'},
            'docfile': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '25', 'blank': 'True'})
        },
        'anytable_v1.event': {
            'Meta': {'object_name': 'Event'},
            'QR': ('django.db.models.fields.CharField', [], {'default': "''", 'null': 'True', 'max_length': '1024', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'event_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'event_time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'event title'", 'max_length': '255'}),
            'venue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anytable_v1.Venue']"})
        },
        'anytable_v1.eventprice': {
            'Meta': {'object_name': 'EventPrice'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anytable_v1.Event']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '50', 'blank': 'True'}),
            'price_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anytable_v1.PriceType']"})
        },
        'anytable_v1.folder': {
            'Meta': {'object_name': 'Folder'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['anytable_v1.Folder']", 'blank': 'True'})
        },
        'anytable_v1.pricetype': {
            'Meta': {'object_name': 'PriceType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '255', 'blank': 'True'})
        },
        'anytable_v1.region': {
            'Meta': {'object_name': 'Region'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'})
        },
        'anytable_v1.subscriber': {
            'Meta': {'object_name': 'Subscriber'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logIn': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'password': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'})
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
            'email': ('django.db.models.fields.EmailField', [], {'db_index': 'True', 'max_length': '75', 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.NullBooleanField', [], {'default': 'False', 'null': 'True', 'blank': 'True'}),
            'joined': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True'})
        },
        'anytable_v1.venue': {
            'Meta': {'object_name': 'Venue'},
            'address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['anytable_v1.City']"}),
            'cropping': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'facebook_url': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '1024', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'instagram': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '1024', 'blank': 'True'}),
            'kitchen': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['anytable_v1.VenueKitchen']", 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'option': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'null': 'True', 'to': "orm['anytable_v1.VenueOptions']"}),
            'schedule': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'subscriber': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['anytable_v1.Subscriber']"}),
            'tel': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '1024', 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['anytable_v1.VenueType']"}),
            'vk_url': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '1024', 'blank': 'True'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'anytable_v1.venueadministrator': {
            'Meta': {'object_name': 'VenueAdministrator'},
            'active': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'venue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anytable_v1.Venue']"})
        },
        'anytable_v1.venueimage': {
            'Meta': {'object_name': 'Venueimage'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'max_length': '100', 'blank': 'True'}),
            'venue': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['anytable_v1.Venue']"})
        },
        'anytable_v1.venuekitchen': {
            'Meta': {'object_name': 'VenueKitchen'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
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