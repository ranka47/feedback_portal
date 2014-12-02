from feedback import models
from django.contrib.auth.models import User, Group, Permission
from django.utils import timezone
from django.forms import ModelForm
from django import forms
from django.forms.extras.widgets import SelectDateWidget
from django.utils.translation import ugettext_lazy as _
# from feedback import selecttimewidget

class PostForm(ModelForm):
    class Meta:
        model = models.Post
        fields = ('post', 'course')

class StudentForm(ModelForm):
    # course = forms.ModelMultipleChoiceField(queryset=models.Course.objects.all())
    class Meta:
        model=models.Student
        fields=('courses',)
    
class CommentForm(ModelForm):
    text = forms.CharField(label='', 
                    widget=forms.Textarea(attrs={'placeholder': 'Enter your comment', 'rows':3, 'cols':105}))
    class Meta:
        model = models.Comment
        fields = ('text',)

class CourseFacultyFeedbackForm(ModelForm):
    class Meta:
        model=models.CourseFacultyLink
        fields=('mid_design','mid_instructor','mid_tutorial','mid_exam','end_design','end_instructor','end_tutorial','end_exam',)

class MidSemFeedbackForm(ModelForm):
    class Meta:
        model=models.CourseFacultyLink
        fields=('design','instructor','tutorial','exam',)

class EndSemFeedbackForm(ModelForm):
    class Meta:
        model=models.CourseFacultyLink
        fields=('design','instructor','tutorial','exam',)
        