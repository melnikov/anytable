# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'VenueAdmin'
        db.create_table('anytable_v1_venueadmin', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=254)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('venue', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anytable_v1.Venue'])),
            ('active', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal('anytable_v1', ['VenueAdmin'])


        # Changing field 'Event.venue'
        db.alter_column('anytable_v1_event', 'venue_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anytable_v1.Venue']))

        # Changing field 'User.city'
        db.alter_column('anytable_v1_user', 'city_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anytable_v1.City']))

        # Changing field 'User.is_admin'
        db.alter_column('anytable_v1_user', 'is_admin', self.gf('django.db.models.fields.NullBooleanField')(null=True))

        # Changing field 'City.region'
        db.alter_column('anytable_v1_city', 'region_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anytable_v1.Region']))

        # Changing field 'Venue.city'
        db.alter_column('anytable_v1_venue', 'city_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anytable_v1.City'], null=True))

        # Changing field 'Venue.subscriber'
        db.alter_column('anytable_v1_venue', 'subscriber_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anytable_v1.Subscriber'], null=True))

        # Changing field 'Venueimage.venue'
        db.alter_column('anytable_v1_venueimage', 'venue_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anytable_v1.Venue'], null=True))

    def backwards(self, orm):
        # Deleting model 'VenueAdmin'
        db.delete_table('anytable_v1_venueadmin')


        # Changing field 'Event.venue'
        db.alter_column('anytable_v1_event', 'venue_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anytable_v1.venue']))

        # Changing field 'User.city'
        db.alter_column('anytable_v1_user', 'city_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anytable_v1.city']))

        # Changing field 'User.is_admin'
        db.alter_column('anytable_v1_user', 'is_admin', self.gf('django.db.models.fields.BooleanField')())

        # Changing field 'City.region'
        db.alter_column('anytable_v1_city', 'region_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anytable_v1.region']))

        # Changing field 'Venue.city'
        db.alter_column('anytable_v1_venue', 'city_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anytable_v1.city'], null=True))

        # Changing field 'Venue.subscriber'
        db.alter_column('anytable_v1_venue', 'subscriber_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anytable_v1.subscriber'], null=True))

        # Changing field 'Venueimage.venue'
        db.alter_column('anytable_v1_venueimage', 'venue_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anytable_v1.venue'], null=True))

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
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'venue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anytable_v1.Venue']"})
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
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'db_index': 'True', 'max_length': '75'}),
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
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anytable_v1.City']", 'null': 'True'}),
            'cropping': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'facebook_url': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'kitchen': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['anytable_v1.VenueKitchen']", 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'option': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['anytable_v1.VenueOptions']", 'null': 'True'}),
            'schedule': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'subscriber': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anytable_v1.Subscriber']", 'null': 'True'}),
            'tel': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['anytable_v1.VenueType']"}),
            'vk_url': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'anytable_v1.venueadmin': {
            'Meta': {'object_name': 'VenueAdmin'},
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
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'venue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anytable_v1.Venue']", 'null': 'True'})
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