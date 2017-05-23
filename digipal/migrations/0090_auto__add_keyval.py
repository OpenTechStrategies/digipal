# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'KeyVal'
        db.create_table(u'digipal_keyval', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(unique=True, max_length=300)),
            ('val', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'digipal', ['KeyVal'])


    def backwards(self, orm):
        # Deleting model 'KeyVal'
        db.delete_table(u'digipal_keyval')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'digipal.allograph': {
            'Meta': {'ordering': "['character__ontograph__sort_order', 'character__ontograph__ontograph_type__name', 'name']", 'unique_together': "(['name', 'character'],)", 'object_name': 'Allograph'},
            'aspects': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['digipal.Aspect']", 'null': 'True', 'blank': 'True'}),
            'character': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['digipal.Character']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'default': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hidden': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'digipal.allographcomponent': {
            'Meta': {'ordering': "['allograph', 'component']", 'object_name': 'AllographComponent'},
            'allograph': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'allograph_components'", 'to': u"orm['digipal.Allograph']"}),
            'component': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['digipal.Component']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'features': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['digipal.Feature']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        },
        u'digipal.alphabet': {
            'Meta': {'ordering': "['name']", 'object_name': 'Alphabet'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'hands': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['digipal.Hand']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'ontographs': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['digipal.Ontograph']", 'null': 'True', 'blank': 'True'})
        },
        u'digipal.annotation': {
            'Meta': {'ordering': "['graph', 'modified']", 'object_name': 'Annotation'},
            'after': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'allograph_after'", 'null': 'True', 'to': u"orm['digipal.Allograph']"}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'before': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'allograph_before'", 'null': 'True', 'to': u"orm['digipal.Allograph']"}),
            'clientid': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '24', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'cutout': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'display_note': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'geo_json': ('django.db.models.fields.TextField', [], {}),
            'graph': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['digipal.Graph']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'holes': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['digipal.Image']", 'null': 'True'}),
            'internal_note': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'rotation': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['digipal.Status']", 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '15', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'vector_id': ('django.db.models.fields.TextField', [], {'default': "u''", 'blank': 'True'})
        },
        u'digipal.apitransform': {
            'Meta': {'ordering': "['title']", 'object_name': 'ApiTransform'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mimetype': ('django.db.models.fields.CharField', [], {'default': "'text/xml'", 'max_length': '30'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'sample_request': ('django.db.models.fields.CharField', [], {'default': "'graph'", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '30'}),
            'template': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'webpage': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'digipal.appearance': {
            'Meta': {'ordering': "['sort_order', 'text']", 'object_name': 'Appearance'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legacy_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'digipal.archive': {
            'Meta': {'ordering': "['historical_item']", 'object_name': 'Archive'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dubitable': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'historical_item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['digipal.HistoricalItem']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legacy_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'digipal.aspect': {
            'Meta': {'ordering': "['name']", 'object_name': 'Aspect'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'features': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['digipal.Feature']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        u'digipal.authenticitycategory': {
            'Meta': {'ordering': "['name']", 'object_name': 'AuthenticityCategory'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'})
        },
        u'digipal.carouselitem': {
            'Meta': {'ordering': "['sort_order', 'title']", 'object_name': 'CarouselItem'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'image_alt': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'image_file': ('django.db.models.fields.files.ImageField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'image_title': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        u'digipal.cataloguenumber': {
            'Meta': {'ordering': "['source', 'number']", 'unique_together': "(['source', 'number', 'historical_item', 'text'],)", 'object_name': 'CatalogueNumber'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'historical_item': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'catalogue_numbers'", 'null': 'True', 'to': u"orm['digipal.HistoricalItem']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'number_slug': ('django.db.models.fields.SlugField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['digipal.Source']"}),
            'text': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'catalogue_numbers'", 'null': 'True', 'to': u"orm['digipal.Text']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'digipal.category': {
            'Meta': {'ordering': "['name']", 'object_name': 'Category'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'sort_order': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'digipal.character': {
            'Meta': {'ordering': "['ontograph__sort_order', 'ontograph__ontograph_type__name', 'name']", 'object_name': 'Character'},
            'components': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['digipal.Component']", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'form': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['digipal.CharacterForm']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'ontograph': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['digipal.Ontograph']"}),
            'unicode_point': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'})
        },
        u'digipal.characterform': {
            'Meta': {'ordering': "['name']", 'object_name': 'CharacterForm'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        u'digipal.collation': {
            'Meta': {'ordering': "['historical_item']", 'object_name': 'Collation'},
            'back_flyleaves': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fragment': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'front_flyleaves': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'historical_item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['digipal.HistoricalItem']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'leaves': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        },
        u'digipal.component': {
            'Meta': {'ordering': "['name']", 'object_name': 'Component'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'features': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'components'", 'symmetrical': 'False', 'through': u"orm['digipal.ComponentFeature']", 'to': u"orm['digipal.Feature']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        u'digipal.componentfeature': {
            'Meta': {'ordering': "['component__name', 'feature__name']", 'unique_together': "(['component', 'feature'],)", 'object_name': 'ComponentFeature', 'db_table': "'digipal_component_features'"},
            'component': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['digipal.Component']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'feature': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['digipal.Feature']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'set_by_default': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'digipal.county': {
            'Meta': {'ordering': "['name']", 'object_name': 'County'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legacy_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        u'digipal.currentitem': {
            'Meta': {'ordering': "['repository', 'shelfmark']", 'unique_together': "(['repository', 'shelfmark'],)", 'object_name': 'CurrentItem'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'display_label': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legacy_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'owners': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'current_items'", 'default': 'None', 'to': u"orm['digipal.Owner']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'repository': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['digipal.Repository']"}),
            'shelfmark': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'digipal.date': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'Date'},
            'additional_band': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'band': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'evidence': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legacy_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'legacy_reference': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'max_weight': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'min_weight': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'post_conquest': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            's_xi': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.FloatField', [], {})
        },
        u'digipal.dateevidence': {
            'Meta': {'ordering': "['date']", 'object_name': 'DateEvidence'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['digipal.Date']", 'null': 'True', 'blank': 'True'}),
            'date_description': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'evidence': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'hand': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['digipal.Hand']", 'null': 'True', 'blank': 'True'}),
            'historical_item': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'date_evidences'", 'null': 'True', 'blank': 'True', 'to': u"orm['digipal.HistoricalItem']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_firm_date': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'legacy_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'reference': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['digipal.Reference']", 'null': 'True', 'blank': 'True'})
        },
        u'digipal.decoration': {
            'Meta': {'ordering': "['historical_item']", 'object_name': 'Decoration'},
            'catalogue_references': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'colours': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'decorated': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'historical_item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['digipal.HistoricalItem']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'illuminated': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'illustrated': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'inks': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'num_colours': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'num_inks': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'style': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        },
        u'digipal.description': {
            'Meta': {'ordering': "['historical_item', 'text']", 'unique_together': "(['source', 'historical_item', 'text'],)", 'object_name': 'Description'},
            'comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'historical_item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['digipal.HistoricalItem']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['digipal.Source']"}),
            'summary': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'descriptions'", 'null': 'True', 'to': u"orm['digipal.Text']"})
        },
        u'digipal.feature': {
            'Meta': {'ordering': "['name']", 'object_name': 'Feature'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'})
        },
        u'digipal.format': {
            'Meta': {'ordering': "['name']", 'object_name': 'Format'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legacy_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        u'digipal.graph': {
            'Meta': {'ordering': "['idiograph']", 'object_name': 'Graph'},
            'aspects': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['digipal.Aspect']", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'display_label': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'parts'", 'null': 'True', 'to': u"orm['digipal.Graph']"}),
            'hand': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'graphs'", 'to': u"orm['digipal.Hand']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idiograph': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['digipal.Idiograph']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        },
        u'digipal.graphcomponent': {
            'Meta': {'ordering': "['graph', 'component']", 'object_name': 'GraphComponent'},
            'component': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['digipal.Component']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'features': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['digipal.Feature']", 'symmetrical': 'False'}),
            'graph': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'graph_components'", 'to': u"orm['digipal.Graph']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        },
        u'digipal.hair': {
            'Meta': {'ordering': "['label']", 'object_name': 'Hair'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'legacy_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        },
        u'digipal.hand': {
            'Meta': {'ordering': "['item_part', 'num']", 'object_name': 'Hand'},
            'appearance': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['digipal.Appearance']", 'null': 'True', 'blank': 'True'}),
            'assigned_date': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['digipal.Date']", 'null': 'True', 'blank': 'True'}),
            'assigned_place': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['digipal.Place']", 'null': 'True', 'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'display_label': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'display_note': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'em_title': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'gloss_only': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'glossed_text': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['digipal.Category']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'hands'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['digipal.Image']"}),
            'imitative': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'internal_note': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'item_part': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'hands'", 'to': u"orm['digipal.ItemPart']"}),
            'ker': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'label': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'latin_only': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'latin_style': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['digipal.LatinStyle']", 'null': 'True', 'blank': 'True'}),
            'legacy_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'locus': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'membra_disjecta': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'num': ('django.db.models.fields.IntegerField', [], {}),
            'num_glosses': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'num_glossing_hands': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'relevant': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'scragg': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'}),
            'scribble_only': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'scribe': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'hands'", 'null': 'True', 'to': u"orm['digipal.Scribe']"}),
            'script': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['digipal.Script']", 'null': 'True', 'blank': 'True'}),
            'selected_locus': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'stewart_record': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'hands'", 'null': 'True', 'to': u"orm['digipal.StewartRecord']"}),
            'surrogates': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'digipal.handdescription': {
            'Meta': {'ordering': "['hand', 'source__priority']", 'object_name': 'HandDescription'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'hand': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'descriptions'", 'null': 'True', 'to': u"orm['digipal.Hand']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'hand_descriptions'", 'null': 'True', 'to': u"orm['digipal.Source']"})
        },
        u'digipal.historicalitem': {
            'Meta': {'ordering': "['display_label', 'date', 'name']", 'object_name': 'HistoricalItem'},
            'catalogue_number': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['digipal.Category']", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'date_sort': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'display_label': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'hair': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['digipal.Hair']", 'null': 'True', 'blank': 'True'}),
            'historical_item_format': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['digipal.Format']", 'null': 'True', 'blank': 'True'}),
            'historical_item_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['digipal.HistoricalItemType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['digipal.Language']", 'null': 'True', 'blank': 'True'}),
            'legacy_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'legacy_reference': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'neumed': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'owners': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['digipal.Owner']", 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'vernacular': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'})
        },
        u'digipal.historicalitemdate': {
            'Meta': {'ordering': "['date']", 'object_name': 'HistoricalItemDate'},
            'addition': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['digipal.Date']"}),
            'dubitable': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'evidence': ('django.db.models.fields.TextField', [], {}),
            'historical_item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['digipal.HistoricalItem']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legacy_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'vernacular': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'})
        },
        u'digipal.historicalitemtype': {
            'Meta': {'ordering': "['name']", 'object_name': 'HistoricalItemType'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'digipal.idiograph': {
            'Meta': {'ordering': "['allograph']", 'object_name': 'Idiograph'},
            'allograph': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['digipal.Allograph']"}),
            'aspects': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['digipal.Aspect']", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'display_label': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'scribe': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'idiographs'", 'null': 'True', 'to': u"orm['digipal.Scribe']"})
        },
        u'digipal.idiographcomponent': {
            'Meta': {'ordering': "['idiograph', 'component']", 'object_name': 'IdiographComponent'},
            'component': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['digipal.Component']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'features': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['digipal.Feature']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idiograph': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['digipal.Idiograph']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        },
        u'digipal.image': {
            'Meta': {'ordering': "['item_part__display_label', 'folio_number', 'folio_side']", 'object_name': 'Image'},
            'annotation_status': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'images'", 'null': 'True', 'blank': 'True', 'to': u"orm['digipal.ImageAnnotationStatus']"}),
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'custom_label': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'display_label': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'folio_number': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'folio_side': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iipimage': ('iipimage.fields.ImageField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'internal_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'item_part': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'images'", 'null': 'True', 'blank': 'True', 'to': u"orm['digipal.ItemPart']"}),
            u'keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'locus': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '64', 'blank': 'True'}),
            'media_permission': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['digipal.MediaPermission']", 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'page_boundaries': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'quire': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'size': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'transcription': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'width': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'digipal.imageannotationstatus': {
            'Meta': {'ordering': "['name']", 'object_name': 'ImageAnnotationStatus'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        u'digipal.institution': {
            'Meta': {'ordering': "['name']", 'object_name': 'Institution'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'foundation': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'founder': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'person_founder'", 'null': 'True', 'to': u"orm['digipal.Person']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institution_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['digipal.InstitutionType']"}),
            'legacy_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'patron': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'person_patron'", 'null': 'True', 'to': u"orm['digipal.Person']"}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['digipal.Place']"}),
            'reformer': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'person_reformer'", 'null': 'True', 'to': u"orm['digipal.Person']"}),
            'refoundation': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'})
        },
        u'digipal.institutiontype': {
            'Meta': {'ordering': "['name']", 'object_name': 'InstitutionType'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'digipal.itemorigin': {
            'Meta': {'ordering': "['historical_item']", 'object_name': 'ItemOrigin'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dubitable': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'evidence': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'historical_item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['digipal.HistoricalItem']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institution': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'item_origins'", 'null': 'True', 'to': u"orm['digipal.Institution']"}),
            'legacy_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'item_origins'", 'null': 'True', 'to': u"orm['digipal.Place']"})
        },
        u'digipal.itempart': {
            'Meta': {'ordering': "['display_label']", 'object_name': 'ItemPart'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'current_item': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['digipal.CurrentItem']", 'null': 'True', 'blank': 'True'}),
            'display_label': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'subdivisions'", 'null': 'True', 'to': u"orm['digipal.ItemPart']"}),
            'group_locus': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'historical_items': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'item_parts'", 'symmetrical': 'False', 'through': u"orm['digipal.ItemPartItem']", 'to': u"orm['digipal.HistoricalItem']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'locus': ('django.db.models.fields.CharField', [], {'default': "'face'", 'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'owners': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['digipal.Owner']", 'null': 'True', 'blank': 'True'}),
            'pagination': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['digipal.ItemPartType']", 'null': 'True', 'blank': 'True'})
        },
        u'digipal.itempartauthenticity': {
            'Meta': {'unique_together': "(['item_part', 'category', 'source'],)", 'object_name': 'ItemPartAuthenticity'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'itempart_authenticity'", 'to': u"orm['digipal.AuthenticityCategory']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_part': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'authenticities'", 'to': u"orm['digipal.ItemPart']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'itempart_authenticity'", 'null': 'True', 'to': u"orm['digipal.Source']"})
        },
        u'digipal.itempartitem': {
            'Meta': {'ordering': "['historical_item__id']", 'object_name': 'ItemPartItem'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'historical_item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'partitions'", 'to': u"orm['digipal.HistoricalItem']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_part': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'constitutionalities'", 'to': u"orm['digipal.ItemPart']"}),
            'locus': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '64', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        },
        u'digipal.itemparttype': {
            'Meta': {'ordering': "['name']", 'object_name': 'ItemPartType'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        u'digipal.keyval': {
            'Meta': {'object_name': 'KeyVal'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '300'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'val': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'digipal.language': {
            'Meta': {'ordering': "['name']", 'object_name': 'Language'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legacy_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        u'digipal.latinstyle': {
            'Meta': {'ordering': "['style']", 'object_name': 'LatinStyle'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legacy_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'style': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'digipal.layout': {
            'Meta': {'ordering': "['item_part', 'historical_item']", 'object_name': 'Layout'},
            'bilinear_ruling': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'columns': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'frame_height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'frame_width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hair_arrangement': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['digipal.Hair']", 'null': 'True', 'blank': 'True'}),
            'historical_item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['digipal.HistoricalItem']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insular_pricking': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'item_part': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'layouts'", 'null': 'True', 'to': u"orm['digipal.ItemPart']"}),
            'lines': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'multiple_sheet_rulling': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'on_top_line': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'page_height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'page_width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tramline_width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'digipal.measurement': {
            'Meta': {'ordering': "['label']", 'object_name': 'Measurement'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'legacy_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        },
        u'digipal.mediapermission': {
            'Meta': {'ordering': "['label']", 'object_name': 'MediaPermission'},
            'display_message': ('tinymce.models.HTMLField', [], {'default': "''", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'permission': ('django.db.models.fields.IntegerField', [], {'default': '100'})
        },
        u'digipal.ontograph': {
            'Meta': {'ordering': "['sort_order', 'ontograph_type__name', 'name']", 'unique_together': "(['name', 'ontograph_type'],)", 'object_name': 'Ontograph'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'nesting_level': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ontograph_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['digipal.OntographType']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'digipal.ontographtype': {
            'Meta': {'ordering': "['name']", 'object_name': 'OntographType'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        u'digipal.owner': {
            'Meta': {'ordering': "['date']", 'object_name': 'Owner'},
            'annotated': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'display_label': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'blank': 'True'}),
            'dubitable': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'evidence': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institution': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'owners'", 'null': 'True', 'blank': 'True', 'to': u"orm['digipal.Institution']"}),
            'legacy_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'owners'", 'null': 'True', 'blank': 'True', 'to': u"orm['digipal.Person']"}),
            'rebound': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'repository': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'owners'", 'null': 'True', 'blank': 'True', 'to': u"orm['digipal.Repository']"})
        },
        u'digipal.ownertype': {
            'Meta': {'ordering': "['name']", 'object_name': 'OwnerType'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'digipal.person': {
            'Meta': {'ordering': "['name']", 'object_name': 'Person'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legacy_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '256'})
        },
        u'digipal.place': {
            'Meta': {'ordering': "['name']", 'object_name': 'Place'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'current_county': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'county_current'", 'null': 'True', 'to': u"orm['digipal.County']"}),
            'eastings': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'historical_county': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'county_historical'", 'null': 'True', 'to': u"orm['digipal.County']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legacy_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'northings': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'other_names': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['digipal.Region']", 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['digipal.PlaceType']", 'null': 'True', 'blank': 'True'})
        },
        u'digipal.placeevidence': {
            'Meta': {'ordering': "['place']", 'object_name': 'PlaceEvidence'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'evidence': ('django.db.models.fields.TextField', [], {}),
            'hand': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['digipal.Hand']", 'null': 'True', 'blank': 'True'}),
            'historical_item': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['digipal.HistoricalItem']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legacy_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['digipal.Place']"}),
            'place_description': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'reference': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['digipal.Reference']"}),
            'written_as': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'})
        },
        u'digipal.placetype': {
            'Meta': {'ordering': "['name']", 'object_name': 'PlaceType'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'digipal.proportion': {
            'Meta': {'ordering': "['hand', 'measurement']", 'object_name': 'Proportion'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'cue_height': ('django.db.models.fields.FloatField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'hand': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['digipal.Hand']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legacy_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'measurement': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['digipal.Measurement']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'value': ('django.db.models.fields.FloatField', [], {})
        },
        u'digipal.reference': {
            'Meta': {'ordering': "['name']", 'unique_together': "(['name', 'name_index'],)", 'object_name': 'Reference'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'full_reference': ('tinymce.models.HTMLField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legacy_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'legacy_reference': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'name_index': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'})
        },
        u'digipal.region': {
            'Meta': {'ordering': "['name']", 'object_name': 'Region'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        u'digipal.repository': {
            'Meta': {'ordering': "['short_name', 'name']", 'object_name': 'Repository'},
            'british_isles': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'comma': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'copyright_notice': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'digital_project': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legacy_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'media_permission': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['digipal.MediaPermission']", 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'part_of': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'parts'", 'null': 'True', 'blank': 'True', 'to': u"orm['digipal.Repository']"}),
            'place': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['digipal.Place']"}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'repositories'", 'null': 'True', 'blank': 'True', 'to': u"orm['digipal.OwnerType']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'digipal.requestlog': {
            'Meta': {'object_name': 'RequestLog'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'request': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'result_count': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'digipal.scribe': {
            'Meta': {'ordering': "['name']", 'object_name': 'Scribe'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legacy_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'legacy_reference': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'reference': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['digipal.Reference']", 'null': 'True', 'blank': 'True'}),
            'scriptorium': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['digipal.Institution']", 'null': 'True', 'blank': 'True'})
        },
        u'digipal.script': {
            'Meta': {'ordering': "['name']", 'object_name': 'Script'},
            'allographs': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['digipal.Allograph']", 'symmetrical': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legacy_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'digipal.scriptcomponent': {
            'Meta': {'ordering': "['script', 'component']", 'object_name': 'ScriptComponent'},
            'component': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['digipal.Component']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'features': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['digipal.Feature']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'script': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['digipal.Script']"})
        },
        u'digipal.source': {
            'Meta': {'ordering': "['name']", 'object_name': 'Source'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'label_slug': ('django.db.models.fields.SlugField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'label_styled': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'digipal.status': {
            'Meta': {'ordering': "['name']", 'object_name': 'Status'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'default': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'})
        },
        u'digipal.stewartrecord': {
            'Meta': {'ordering': "['scragg']", 'object_name': 'StewartRecord'},
            'adate': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'cartulary': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'charter': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'contents': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'eel': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'em': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '800', 'null': 'True', 'blank': 'True'}),
            'fols': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'glosses': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'gneuss': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '300', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'import_messages': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'ker': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'ker_hand': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'locus': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'matched_hands': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'minor': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '600', 'null': 'True', 'blank': 'True'}),
            'repository': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'scragg': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'selected': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'shelf_mark': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'sp': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'stokes_db': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'surrogates': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '300', 'null': 'True', 'blank': 'True'})
        },
        u'digipal.text': {
            'Meta': {'ordering': "['name']", 'unique_together': "(['name'],)", 'object_name': 'Text'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'texts'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['digipal.Category']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_parts': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'texts'", 'symmetrical': 'False', 'through': u"orm['digipal.TextItemPart']", 'to': u"orm['digipal.ItemPart']"}),
            'languages': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'texts'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['digipal.Language']"}),
            'legacy_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'digipal.textitempart': {
            'Meta': {'unique_together': "(['item_part', 'text'],)", 'object_name': 'TextItemPart'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_part': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'text_instances'", 'to': u"orm['digipal.ItemPart']"}),
            'locus': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'text_instances'", 'to': u"orm['digipal.Text']"})
        }
    }

    complete_apps = ['digipal']