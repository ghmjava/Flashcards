# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-04 08:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dictionary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'Dictionaries',
            },
        ),
        migrations.CreateModel(
            name='Flashcard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=30)),
                ('translation', models.CharField(max_length=30)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Flashcards_Dictionary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hits', models.IntegerField(default=0)),
                ('successes', models.IntegerField(default=0)),
                ('last_hit', models.DateTimeField(null=True)),
                ('last_success', models.DateTimeField(null=True)),
                ('dictionary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flashcards.Dictionary')),
                ('flashcard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flashcards.Flashcard')),
            ],
            options={
                'verbose_name_plural': 'Dictionary flashcards',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=3)),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='flashcard',
            name='dictionaries',
            field=models.ManyToManyField(through='flashcards.Flashcards_Dictionary', to='flashcards.Dictionary'),
        ),
        migrations.AddField(
            model_name='flashcard',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='language', to='flashcards.Language'),
        ),
        migrations.AddField(
            model_name='flashcard',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='flashcard',
            name='translation_language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translation_language', to='flashcards.Language'),
        ),
        migrations.AddField(
            model_name='dictionary',
            name='flashcards',
            field=models.ManyToManyField(through='flashcards.Flashcards_Dictionary', to='flashcards.Flashcard'),
        ),
        migrations.AddField(
            model_name='dictionary',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dictionaries', to=settings.AUTH_USER_MODEL),
        ),
    ]
