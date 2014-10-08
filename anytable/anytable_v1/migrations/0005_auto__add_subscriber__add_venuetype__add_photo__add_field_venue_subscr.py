# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'subscriber'
        db.create_table('anytable_v1_subscriber', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('logIn', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('password', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
        ))
        db.send_create_signal('anytable_v1', ['subscriber'])

        # Adding model 'venueType'
        db.create_table('anytable_v1_venuetype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('anytable_v1', ['venueType'])

        # Adding model 'photo'
        db.create_table('anytable_v1_photo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(null=True, blank=True, max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('anytable_v1', ['photo'])

        # Adding field 'venue.subscriber'
        db.add_column('anytable_v1_venue', 'subscriber',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anytable_v1.subscriber'], null=True),
                      keep_default=False)

        # Adding field 'venue.type'
        db.add_column('anytable_v1_venue', 'type',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anytable_v1.venueType'], null=True),
                      keep_default=False)

        # Adding field 'venue.city'
        db.add_column('anytable_v1_venue', 'city',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['anytable_v1.city'], null=True),
                      keep_default=False)

        # Adding M2M table for field photo on 'venue'
        m2m_table_name = db.shorten_name('anytable_v1_venue_photo')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('venue', models.ForeignKey(orm['anytable_v1.venue'], null=False)),
            ('photo', models.ForeignKey(orm['anytable_v1.photo'], null=False))
        ))
        db.create_unique(m2m_table_name, ['venue_id', 'photo_id'])

        # Deleting field 'event.image'
        db.delete_column('anytable_v1_event', 'image')

        # Adding M2M table for field photo on 'event'
        m2m_table_name = db.shorten_name('anytable_v1_event_photo')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm['anytable_v1.event'], null=False)),
            ('photo', models.ForeignKey(orm['anytable_v1.photo'], null=False))
        ))
        db.create_unique(m2m_table_name, ['event_id', 'photo_id'])


    def backwards(self, orm):
        # Deleting model 'subscriber'
        db.delete_table('anytable_v1_subscriber')

        # Deleting model 'venueType'
        db.delete_table('anytable_v1_venuetype')

        # Deleting model 'photo'
        db.delete_table('anytable_v1_photo')

        # Deleting field 'venue.subscriber'
        db.delete_column('anytable_v1_venue', 'subscriber_id')

        # Deleting field 'venue.type'
        db.delete_column('anytable_v1_venue', 'type_id')

        # Deleting field 'venue.city'
        db.delete_column('anytable_v1_venue', 'city_id')

        # Removing M2M table for field photo on 'venue'
        db.delete_table(db.shorten_name('anytable_v1_venue_photo'))

        # Adding field 'event.image'
        db.add_column('anytable_v1_event', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(null=True, blank=True, max_length=100),
                      keep_default=False)

        # Removing M2M table for field photo on 'event'
        db.delete_table(db.shorten_name('anytable_v1_event_photo'))


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
            'photo': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['anytable_v1.photo']", 'symmetrical': 'False'}),
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
        'anytable_v1.venue': {
            'Meta': {'object_name': 'venue'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['anytable_v1.city']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'null': 'True', 'blank': 'True', 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'photo': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['anytable_v1.photo']", 'symmetrical': 'False'}),
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