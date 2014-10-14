# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'testUsers'
        db.create_table('anytable_v1_testusers', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('firstName', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('lastName', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('anytable_v1', ['testUsers'])

        # Adding model 'testCities'
        db.create_table('anytable_v1_testcities', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('population', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('anytable_v1', ['testCities'])

        # Adding model 'venue'
        db.create_table('anytable_v1_venue', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('anytable_v1', ['venue'])

        # Adding model 'event'
        db.create_table('anytable_v1_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('imagePath', self.gf('django.db.models.fields.CharField')(max_length=1024, default='')),
            ('QR', self.gf('django.db.models.fields.CharField')(max_length=1024, default='')),
            ('QR2', self.gf('django.db.models.fields.CharField')(max_length=1024, default='')),
            ('venue', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anytable_v1.venue'])),
        ))
        db.send_create_signal('anytable_v1', ['event'])

        # Adding model 'region'
        db.create_table('anytable_v1_region', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, default='')),
            ('name2', self.gf('django.db.models.fields.CharField')(max_length=255, default='')),
        ))
        db.send_create_signal('anytable_v1', ['region'])

        # Adding model 'city'
        db.create_table('anytable_v1_city', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anytable_v1.region'])),
        ))
        db.send_create_signal('anytable_v1', ['city'])


    def backwards(self, orm):
        # Deleting model 'testUsers'
        db.delete_table('anytable_v1_testusers')

        # Deleting model 'testCities'
        db.delete_table('anytable_v1_testcities')

        # Deleting model 'venue'
        db.delete_table('anytable_v1_venue')

        # Deleting model 'event'
        db.delete_table('anytable_v1_event')

        # Deleting model 'region'
        db.delete_table('anytable_v1_region')

        # Deleting model 'city'
        db.delete_table('anytable_v1_city')


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
            'QR2': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'default': "''"}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagePath': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'default': "''"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'venue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anytable_v1.venue']"})
        },
        'anytable_v1.region': {
            'Meta': {'object_name': 'region'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'default': "''"}),
            'name2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'default': "''"})
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