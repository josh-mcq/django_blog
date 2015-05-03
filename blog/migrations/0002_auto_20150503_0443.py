# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Blog',
            new_name='Post',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='posted',
            new_name='pub_date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='body',
            new_name='text',
        ),
    ]
