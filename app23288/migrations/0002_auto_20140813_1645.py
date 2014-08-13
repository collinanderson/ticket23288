# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models, migrations


def dump_data(apps, schema_editor):
   Team = apps.get_model('app23288', 'Team')
   sql = unicode(Team(id=8).the_m2m.all().query)
   assert 'the_fk' not in sql, sql


class Migration(migrations.Migration):

   dependencies = [
      ('app23288', '0001_initial'),
   ]

   operations = [
      migrations.RunPython(dump_data),
   ]
