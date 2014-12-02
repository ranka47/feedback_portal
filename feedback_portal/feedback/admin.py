from django.contrib import admin
from feedback.models import Post, Feedback, Course, CourseFacultyLink, CourseStudentLink, Student, Faculty
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class PostAdmin(admin.ModelAdmin):
    list_display = ('student', 'course')

class CourseStudentLinkInline(admin.TabularInline):

    model = CourseStudentLink
    extra = 1


class CourseFacultyLinkInline(admin.TabularInline):

    model = CourseFacultyLink
    extra = 1

class StudentInline(admin.StackedInline):
	model=Student
	can_delete=False		

class StudentAdmin(admin.ModelAdmin):
    inlines = [
        CourseStudentLinkInline,	
    ]

class CourseAdmin(admin.ModelAdmin):
	inlines = [
		CourseFacultyLinkInline,
	]

# class TaskAdmin(admin.ModelAdmin):
#     readonly_fields = ('user_name',)
admin.site.register(Feedback)
admin.site.register(Course,CourseAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Faculty	)
admin.site.register(CourseStudentLink)
admin.site.register(CourseFacultyLink)
admin.site.register(Post, PostAdmin)
