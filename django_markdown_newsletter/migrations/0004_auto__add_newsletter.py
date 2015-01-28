# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Newsletter'
        db.create_table(u'subscribenews_newsletter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('attachement', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'subscribenews', ['Newsletter'])


    def backwards(self, orm):
        # Deleting model 'Newsletter'
        db.delete_table(u'subscribenews_newsletter')


    models = {
        u'subscribenews.newsletter': {
            'Meta': {'object_name': 'Newsletter'},
            'attachement': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'body': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        u'subscribenews.subscribe': {
            'Meta': {'object_name': 'Subscribe'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.CharField', [], {'default': "'ABC'", 'max_length': '120'}),
            'newsletter': ('django.db.models.fields.CharField', [], {'default': "'newsletter'", 'max_length': '20'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['subscribenews']