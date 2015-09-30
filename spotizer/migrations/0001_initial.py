# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('image', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Artiste',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Morceau',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=200)),
                ('file', models.FileField(upload_to=b'')),
                ('album', models.ForeignKey(to='spotizer.Album')),
            ],
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('style', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='artiste',
            name='style',
            field=models.ForeignKey(to='spotizer.Style'),
        ),
        migrations.AddField(
            model_name='album',
            name='artiste',
            field=models.ForeignKey(to='spotizer.Artiste'),
        ),
    ]
