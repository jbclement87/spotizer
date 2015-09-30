# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spotizer', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='morceau',
            options={'verbose_name_plural': 'morceaux'},
        ),
        migrations.AlterField(
            model_name='morceau',
            name='file',
            field=models.FileField(upload_to=b'media/mp3'),
        ),
    ]
