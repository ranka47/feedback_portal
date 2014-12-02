# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.CharField(max_length=50)),
                ('text', models.TextField(default=b'')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('code', models.CharField(max_length=5)),
                ('faculty_number', models.PositiveSmallIntegerField()),
                ('tutorial', models.BooleanField(default=False)),
                ('year', models.DateField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CourseFacultyLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('design', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('instructor', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('tutorial', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('exam', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('year', models.DateField(auto_now_add=True)),
                ('mid_design', models.BooleanField(default=False)),
                ('mid_instructor', models.BooleanField(default=False)),
                ('mid_tutorial', models.BooleanField(default=False)),
                ('mid_exam', models.BooleanField(default=False)),
                ('end_design', models.BooleanField(default=False)),
                ('end_instructor', models.BooleanField(default=False)),
                ('end_tutorial', models.BooleanField(default=False)),
                ('end_exam', models.BooleanField(default=False)),
                ('create', models.PositiveSmallIntegerField(default=0)),
                ('course', models.ForeignKey(to='feedback.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CourseStudentLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course', models.ForeignKey(to='feedback.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mid_design', models.BooleanField(default=False)),
                ('mid_instructor', models.BooleanField(default=False)),
                ('mid_tutorial', models.BooleanField(default=False)),
                ('mid_exam', models.BooleanField(default=False)),
                ('end_design', models.BooleanField(default=False)),
                ('end_instructor', models.BooleanField(default=False)),
                ('end_tutorial', models.BooleanField(default=False)),
                ('end_exam', models.BooleanField(default=False)),
                ('mid_design_value', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('mid_instructor_value', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('mid_tutorial_value', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('mid_exam_value', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('end_design_value', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('end_instructor_value', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('end_tutorial_value', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('end_exam_value', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('post', models.TextField(default=b'')),
                ('coursefaculty', models.ForeignKey(to='feedback.CourseFacultyLink')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('post', models.TextField(default=b'')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(to='feedback.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('roll_id', models.IntegerField()),
                ('courses', models.ManyToManyField(to='feedback.Course', through='feedback.CourseStudentLink')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='post',
            name='student',
            field=models.ForeignKey(to='feedback.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='feedback',
            name='student',
            field=models.ForeignKey(to='feedback.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='coursestudentlink',
            name='student',
            field=models.ForeignKey(to='feedback.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='coursefacultylink',
            name='faculty',
            field=models.ForeignKey(to='feedback.Faculty'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='faculty',
            field=models.ManyToManyField(to='feedback.Faculty', through='feedback.CourseFacultyLink'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='task',
            field=models.ForeignKey(to='feedback.Post'),
            preserve_default=True,
        ),
    ]
