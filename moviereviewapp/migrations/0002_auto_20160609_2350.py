# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-09 23:50
from __future__ import unicode_literals

from django.db import migrations

import csv


def datarater(apps,schema_editor):
    Rater = apps.get_model('moviereviewapp','Rater')
    with open('/Users/chucklapress/tiy-projects/movie_review/movie_review/u.user', 'r') as infile:
        data = csv.reader(infile, delimiter='|')
        for row in data:
            Rater.objects.create(id=row[0], age=row[1], gender=row[2], occupation=row[3], zipcode=row[4])




class Migration(migrations.Migration):

    dependencies = [
        ('moviereviewapp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(datarater)

    ]
