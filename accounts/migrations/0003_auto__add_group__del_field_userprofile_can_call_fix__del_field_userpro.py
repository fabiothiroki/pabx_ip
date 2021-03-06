# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Group'
        db.create_table('accounts_group', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('can_call_ramal', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('can_call_emergency', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('can_call_fix', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('can_call_mobile', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('can_call_ddd', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('can_call_ddi', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('can_call_0800', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('can_call_0300', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('accounts', ['Group'])

        # Deleting field 'UserProfile.can_call_fix'
        db.delete_column('accounts_userprofile', 'can_call_fix')

        # Deleting field 'UserProfile.can_call_0300'
        db.delete_column('accounts_userprofile', 'can_call_0300')

        # Deleting field 'UserProfile.can_call_ddi'
        db.delete_column('accounts_userprofile', 'can_call_ddi')

        # Deleting field 'UserProfile.can_call_ddd'
        db.delete_column('accounts_userprofile', 'can_call_ddd')

        # Deleting field 'UserProfile.can_call_mobile'
        db.delete_column('accounts_userprofile', 'can_call_mobile')

        # Deleting field 'UserProfile.can_call_0800'
        db.delete_column('accounts_userprofile', 'can_call_0800')

        # Adding field 'UserProfile.group'
        db.add_column('accounts_userprofile', 'group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.Group'], null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting model 'Group'
        db.delete_table('accounts_group')

        # Adding field 'UserProfile.can_call_fix'
        db.add_column('accounts_userprofile', 'can_call_fix', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'UserProfile.can_call_0300'
        db.add_column('accounts_userprofile', 'can_call_0300', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'UserProfile.can_call_ddi'
        db.add_column('accounts_userprofile', 'can_call_ddi', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'UserProfile.can_call_ddd'
        db.add_column('accounts_userprofile', 'can_call_ddd', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'UserProfile.can_call_mobile'
        db.add_column('accounts_userprofile', 'can_call_mobile', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'UserProfile.can_call_0800'
        db.add_column('accounts_userprofile', 'can_call_0800', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Deleting field 'UserProfile.group'
        db.delete_column('accounts_userprofile', 'group_id')


    models = {
        'accounts.group': {
            'Meta': {'object_name': 'Group'},
            'can_call_0300': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'can_call_0800': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'can_call_ddd': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'can_call_ddi': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'can_call_emergency': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'can_call_fix': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'can_call_mobile': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'can_call_ramal': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'accounts.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accounts.Group']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'passw': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'ramal': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['accounts']
