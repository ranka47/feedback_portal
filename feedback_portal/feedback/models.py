from django.db import models
from django.contrib.auth.models import User, Group, Permission
from django.utils import timezone
from django.forms import ModelForm
import datetime


class Faculty(models.Model):
    name = models.CharField(max_length=128)
    def __str__(self):
        return self.name

class Course(models.Model):
    name=models.CharField(max_length=128)
    code=models.CharField(max_length=5)
    faculty = models.ForeignKey(Faculty)
    faculty_number=models.PositiveSmallIntegerField()

class Student(models.Model):
    name = models.CharField(max_length=128)
    roll_no=models.IntegerField()
    courses = models.ManyToManyField(Course, through='CourseLink')
    def __str__(self):
        return self.name

class CourseLink(models.Model):
    course = models.ForeignKey(Course)
    student = models.ForeignKey(Student)
    number = models.PositiveSmallIntegerField()
    class Meta:
        ordering = ('number',)
