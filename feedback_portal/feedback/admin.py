from django.contrib import admin
from feedback.models import Course, CourseLink, Student, Faculty

class CourseLinkInline(admin.TabularInline):

    model = CourseLink
    extra = 1

class StudentAdmin(admin.ModelAdmin):
    inlines = [
        CourseLinkInline,
    ]
    

# class TaskAdmin(admin.ModelAdmin):
#     readonly_fields = ('user_name',)

# admin.site.register(Group, GroupAdmin)
admin.site.register(Student, StudentAdmin)
# admin.site.register(Task,TaskAdmin)
admin.site.register(CourseLink)