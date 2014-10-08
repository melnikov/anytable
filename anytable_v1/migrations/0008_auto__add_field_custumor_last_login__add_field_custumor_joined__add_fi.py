# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'custumor.last_login'
        db.add_column('anytable_v1_custumor', 'last_login',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now),
                      keep_default=False)

        # Adding field 'custumor.joined'
        db.add_column('anytable_v1_custumor', 'joined',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True, auto_now_add=True),
                      keep_default=False)

        # Adding field 'custumor.is_active'
        db.add_column('anytable_v1_custumor', 'is_active',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'custumor.is_admin'
        db.add_column('anytable_v1_custumor', 'is_admin',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # Changing field 'custumor.email'
        db.alter_column('anytable_v1_custumor', 'email', self.gf('django.db.models.fields.EmailField')(max_length=75, unique=True))
        # Adding index on 'custumor', fields ['email']
        db.create_index('anytable_v1_custumor', ['email'])

        # Adding unique constraint on 'custumor', fields ['email']
        db.create_unique('anytable_v1_custumor', ['email'])


        # Changing field 'custumor.password'
        db.alter_column('anytable_v1_custumor', 'password', self.gf('django.db.models.fields.CharField')(max_length=128))

    def backwards(self, orm):
        # Removing unique constraint on 'custumor', fields ['email']
        db.delete_unique('anytable_v1_custumor', ['email'])

        # Removing index on 'custumor', fields ['email']
        db.delete_index('anytable_v1_custumor', ['email'])

        # Deleting field 'custumor.last_login'
        db.delete_column('anytable_v1_custumor', 'last_login')

        # Deleting field 'custumor.joined'
        db.delete_column('anytable_v1_custumor', 'joined')

        # Deleting field 'custumor.is_active'
        db.delete_column('anytable_v1_custumor', 'is_active')

        # Deleting field 'custumor.is_admin'
        db.delete_column('anytable_v1_custumor', 'is_admin')


        # Changing field 'custumor.email'
        db.alter_column('anytable_v1_custumor', 'email', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'custumor.password'
        db.alter_column('anytable_v1_custumor', 'password', self.gf('django.db.models.fields.CharField')(max_length=255))

    models = {
        'anytable_v1.city': {
            'Meta': {'object_name': 'city'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anytable_v1.region']"})
        },
        'anytable_v1.custumor': {
            'Meta': {'object_name': 'custumor'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anytable_v1.city']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'unique': 'True', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'joined': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True', 'auto_now_add': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'telephone': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'anytable_v1.event': {
            'Meta': {'object_name': 'event'},
            'QR': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'default': "''"}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'photo': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['anytable_v1.photo']", 'symmetrical': 'False', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'venue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anytable_v1.venue']"})
        },
        'anytable_v1.photo': {
            'Meta': {'object_name': 'photo'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'})
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
        'anytable_v1.venue': {
            'Meta': {'object_name': 'venue'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anytable_v1.city']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'photo': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['anytable_v1.photo']", 'symmetrical': 'False', 'null': 'True', 'blank': 'True'}),
            'subscriber': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anytable_v1.subscriber']", 'null': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anytable_v1.venueType']", 'null': 'True'})
        },
        'anytable_v1.venuetype': {
            'Meta': {'object_name': 'venueType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['anytable_v1']