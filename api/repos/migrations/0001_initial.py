# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-07 15:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import repos.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExternalRepo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('git_url', models.URLField()),
                ('is_public', models.BooleanField(default=True, help_text='If repo is public or private.')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='external_repos', to='projects.Project')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, repos.models.RepoMixin),
        ),
        migrations.CreateModel(
            name='Repo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_public', models.BooleanField(default=True, help_text='If repo is public or private.')),
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='repo', to='projects.Project')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, repos.models.RepoMixin),
        ),
    ]
