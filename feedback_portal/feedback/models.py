from django.db import models
from django.contrib.auth.models import User, Group, Permission
from django.utils import timezone
from django.forms import ModelForm
from django.contrib.auth.models import AbstractBaseUser
import datetime

class Faculty(models.Model):
    user=models.OneToOneField(User)
    name = models.CharField(max_length=128)
    
    def __str__(self):
        return self.name

class Course(models.Model):
    name=models.CharField(max_length=128)
    code=models.CharField(max_length=5)
    faculty = models.ManyToManyField(Faculty, through='CourseFacultyLink')
    faculty_number=models.PositiveSmallIntegerField()
    tutorial=models.BooleanField(default=False)
    year=models.DateField(auto_now_add=True)
    def __str__(self):
        return "%s %s" % (self.name,str(self.year)[:4])

class Student(models.Model):
    user=models.OneToOneField(User)
    roll_id=models.IntegerField()
    courses = models.ManyToManyField(Course, through='CourseStudentLink')
    def __str__(self):
        return self.user.username

class CourseStudentLink(models.Model):
    course = models.ForeignKey(Course)
    student = models.ForeignKey(Student)


class CourseFacultyLink(models.Model):
    course = models.ForeignKey(Course)
    faculty=models.ForeignKey(Faculty)
    # design=models.PositiveSmallIntegerField(blank=True, null=True)
    # instructor=models.PositiveSmallIntegerField(blank=True, null=True)
    # tutorial=models.PositiveSmallIntegerField(blank=True, null=True)
    # exam=models.PositiveSmallIntegerField(blank=True, null=True)
    """Doing due to problem in views.py 'adding' function"""

    design=models.PositiveSmallIntegerField(default=0)
    instructor=models.PositiveSmallIntegerField(default=0)
    tutorial=models.PositiveSmallIntegerField(default=0)
    exam=models.PositiveSmallIntegerField(default=0)
    year=models.DateField(auto_now_add=True)

    mid_design=models.BooleanField(default=False)
    mid_instructor=models.BooleanField(default=False)
    mid_tutorial=models.BooleanField(default=False)
    mid_exam=models.BooleanField(default=False)
    
    end_design=models.BooleanField(default=False)
    end_instructor=models.BooleanField(default=False)
    end_tutorial=models.BooleanField(default=False)
    end_exam=models.BooleanField(default=False)

    create=models.PositiveSmallIntegerField(default=0)
    def __str__(self):
        return "%s : %s : %s" % (self.faculty.name,self.course.name,str(self.year)[:4])

class Post(models.Model):
    student=models.ForeignKey(Student)
    post=models.TextField(default="")
    course=models.ForeignKey(Course)
    created_at=models.DateTimeField(auto_now_add=True, blank=True)

class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=50)
    text = models.TextField(default="")
    task = models.ForeignKey(Post)

class Feedback(models.Model):
    mid_design=models.BooleanField(default=False)
    mid_instructor=models.BooleanField(default=False)
    mid_tutorial=models.BooleanField(default=False)
    mid_exam=models.BooleanField(default=False)

    end_design=models.BooleanField(default=False)
    end_instructor=models.BooleanField(default=False)
    end_tutorial=models.BooleanField(default=False)
    end_exam=models.BooleanField(default=False)

    mid_design_value=models.PositiveSmallIntegerField(blank=True, null=True)
    mid_instructor_value=models.PositiveSmallIntegerField(blank=True, null=True)
    mid_tutorial_value=models.PositiveSmallIntegerField(blank=True, null=True)
    mid_exam_value=models.PositiveSmallIntegerField(blank=True, null=True)

    end_design_value=models.PositiveSmallIntegerField(blank=True, null=True)
    end_instructor_value=models.PositiveSmallIntegerField(blank=True, null=True)
    end_tutorial_value=models.PositiveSmallIntegerField(blank=True, null=True)
    end_exam_value=models.PositiveSmallIntegerField(blank=True, null=True)

    student=models.ForeignKey(Student)
    coursefaculty=models.ForeignKey(CourseFacultyLink)
    post=models.TextField(default="")

    def __str__(self):
        return self.student.user.username
    