from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from django.contrib import auth
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from feedback import forms
from feedback.models import Student, Post, CourseFacultyLink, CourseStudentLink, Feedback
from django.contrib.auth.models import Group, User

def login(request):
    """
    displays login page at the start
    """
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        return render_to_response('feedback/login.html', {'form_errors': form_errors})
    else:
        return render_to_response('feedback/login.html', c)

def auth_view(request):
    """
    Authenticates user from the username and password from POST
    """
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        # Since the user is authenticated, Log the user in.
        auth.login(request, user)
        return HttpResponseRedirect('/feedback/home')

    else:
        # Return an 'invalid login' error message.
        return HttpResponseRedirect('/feedback/')

@login_required(login_url="/feedback")
def logout(request):
    """
    logs out user, only if he is already logged in.
    """
    auth.logout(request)
    return render_to_response('feedback/logout.html')

@login_required(login_url="/feedback/")
def home(request):
    """
    displays home page for user, with his previous tasks
    """
    if not request.user.is_staff: 
        user=User.objects.get(username=request.user.username)
        courses=user.student.courses.all()
        posts=Post.objects.all()
        max_id=0
        for post in posts:
            if post.id > max_id:
                max_id=post.id

        return render_to_response('feedback/home.html', {'max_id':max_id,'courses':courses,'posts':posts,'user':user},context_instance=RequestContext(request))
    else:
        coursefaculty=CourseFacultyLink.objects.all()
        return render_to_response('feedback/home.html',{'coursefaculty':coursefaculty,},context_instance=RequestContext(request))

@login_required(login_url="/feedback/")
def new_post(request):
    if request.method == 'POST':
        form = forms.PostForm(request.POST)
        temp=User.objects.get(username=request.user.username)
        if form.is_valid():
            post=form.save(commit=False)
            for course in temp.student.courses.all():
                if(course == post.course):
                    post.student=temp.student
                    post.save()
                    return render_to_response("feedback/submitted.html", context_instance=RequestContext(request))
            return render_to_response("feedback/new_post.html",{'form':form,'validity':False}, context_instance=RequestContext(request))
    else: 
        form = forms.PostForm()

    return render_to_response("feedback/new_post.html", {'form':form,'validity':True}, context_instance=RequestContext(request))

@login_required(login_url="/feedback")
def logout(request):
    """
    logs out user, only if he is already logged in.
    """
    auth.logout(request)
    return render_to_response('feedback/logout.html')

@login_required(login_url="/feedback/")
def edit_profile(request):
    if request.method == 'POST':
        user=User.objects.get(username=request.user.username)
        user_form=forms.StudentForm(request.POST, instance=user.student)
        if user_form.is_valid():
            form=user_form.save(commit=False)
            for course in form.courses.all():
                CourseStudentLink(course=course, student=user.student).save()
            return render_to_response("feedback/profile.html",{'form':user_form}, context_instance=RequestContext(request))
    else: 
        user=User.objects.get(username=request.user.username)
        form = forms.StudentForm(instance=user.student)

    return render_to_response("feedback/profile.html", {'form':form}, context_instance=RequestContext(request))

@login_required(login_url="/feedback/")
def detail(request,post_id):
    post=Post.objects.get(id=post_id)
    return render(request, 'feedback/post_detail.html', {
                            'post':post,
                            'comment_form': forms.CommentForm,
                            },
                            context_instance=RequestContext(request))
    
@login_required(login_url="/feedback/")
def post_comment(request, post_id):
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            if not Post.objects.get(id=post_id):
                return HttpResponseRedirect('/Permission/home/')
            comment.post = Post.objects.get(id=post_id)
            comment.user = request.user.username
            comment.task_id=post_id
            comment.save()
            url = '/feedback/'
            url += post_id
            url += '/post/'
            return HttpResponseRedirect(url)
    else: 
        return HttpResponseRedirect('/Permission/home/')

@staff_member_required
@login_required(login_url="/feedback/")
def activate_feedback(request, coursefaculty_id):
    if request.method == 'POST':
        temp=CourseFacultyLink.objects.get(id=coursefaculty_id)
        form = forms.CourseFacultyFeedbackForm(request.POST, instance=temp)
        if form.is_valid():
            tempform=form.save(commit=False)
            tempform.mid_design_value=0
            tempform.mid_instructor_value=0
            tempform.mid_tutorial_value=0
            tempform.mid_exam_value=0
            tempform.save()
            admin=User.objects.get(username='admin')
            course=temp.course
            if temp.create == 0:
                for i in CourseStudentLink.objects.all():
                    if course.name==i.course.name:
                        feedback=Feedback(student=i.student,coursefaculty=temp)
                        feedback.save()
            temp.create=1
            temp.save()
            post_desc="There is an update in feedback"+" to "+str(temp.faculty)+" for this course."
            post=Post(student=admin.student,post=post_desc,course=course)
            post.save()
            coursefaculty=CourseFacultyLink.objects.all()
            # return HttpResponse("Yahooooo!")
            return render_to_response("feedback/home.html", {'coursefaculty':coursefaculty,},context_instance=RequestContext(request))
    else: 
        temp=CourseFacultyLink.objects.get(id=coursefaculty_id)
        form = forms.CourseFacultyFeedbackForm(instance=temp)

    return render_to_response("feedback/feedback.html", {'id':coursefaculty_id,'form':form,'temp':temp}, context_instance=RequestContext(request))
    
@login_required(login_url="/feedback/")
def midsem_fillfeedback(request, feedback_id, coursefaculty_id):
    feedback=Feedback.objects.get(id=feedback_id)
    cfl=CourseFacultyLink.objects.get(id=coursefaculty_id)
    if request.method == 'POST':
        form=forms.MidSemFeedbackForm(request.POST,instance=feedback)
        if form.is_valid():
            temp=form.save(commit=False)
            temp.mid_design=cfl.mid_design
            temp.mid_instructor=cfl.mid_instructor
            temp.mid_tutorial=cfl.mid_tutorial
            temp.mid_exam=cfl.mid_exam

            temp.save()
            feedbacks=Feedback.objects.all()
            coursefaculty=CourseFacultyLink.objects.all()
            user=request.user.username
            # return render_to_response("feedback/courses.html",{'user':user,'feedbacks':feedbacks,'coursefaculty':coursefaculty,},context_instance=RequestContext(request))
            return HttpResponseRedirect('/feedback/midsem-feedback/')
    else:
        form=forms.MidSemFeedbackForm(instance=feedback)

    return render_to_response("feedback/midsem_fillfeedback.html",{'form':form, 'feedback':feedback, 'id':coursefaculty_id,},context_instance=RequestContext(request))
    # return HttpResponse("HI")

@login_required(login_url="/feedback/")
def endsem_fillfeedback(request, feedback_id, coursefaculty_id):
    feedback=Feedback.objects.get(id=feedback_id)
    cfl=CourseFacultyLink.objects.get(id=coursefaculty_id)
    if request.method == 'POST':
        form=forms.EndSemFeedbackForm(request.POST,instance=feedback)
        if form.is_valid():
            temp=form.save(commit=False)
            temp.end_design=cfl.end_design
            temp.end_instructor=cfl.end_instructor
            temp.end_tutorial=cfl.end_tutorial
            temp.end_exam=cfl.end_exam


            temp.save()
            feedbacks=Feedback.objects.all()
            coursefaculty=CourseFacultyLink.objects.all()
            user=request.user.username
            # return render_to_response("feedback/courses.html",{'user':user,'feedbacks':feedbacks,'coursefaculty':coursefaculty,},context_instance=RequestContext(request))
            return HttpResponseRedirect('/feedback/endsem-feedback/')
    else:
        form=forms.MidSemFeedbackForm(instance=feedback)

    return render_to_response("feedback/endsem_fillfeedback.html",{'form':form, 'feedback':feedback, 'id':coursefaculty_id,},context_instance=RequestContext(request))
    # return HttpResponse("HI")

@login_required(login_url="/feedback/")
def midsem_feedback(request):
    feedback=Feedback.objects.all()
    coursefaculty=CourseFacultyLink.objects.all()
    user=request.user.username
    return render_to_response("feedback/courses_midsem.html",{'user':user,'feedback':feedback,'coursefaculty':coursefaculty,},context_instance=RequestContext(request))

@login_required(login_url="/feedback/")
def endsem_feedback(request):
    feedback=Feedback.objects.all()
    coursefaculty=CourseFacultyLink.objects.all()
    user=request.user.username
    return render_to_response("feedback/courses_endsem.html",{'user':user,'feedback':feedback,'coursefaculty':coursefaculty,},context_instance=RequestContext(request))

@login_required(login_url="/feedback/")
def comment(request):
    feedbacks=Feedback.objects.all()
    return render_to_response("feedback/comment.html",{'feedbacks':feedbacks,},context_instance=RequestContext(request))

"""Rating only for MidSem"""

def add(coursefaculty,feedback,adding):
    adding.design=adding.design+feedback.mid_design_value
    adding.instructor=adding.instructor+feedback.mid_instructor_value
    adding.tutorial=adding.tutorial+feedback.mid_tutorial_value
    adding.exam=adding.exam+feedback.mid_exam_value
    return adding

@login_required(login_url="/feedback/")
def rating(request):
    feedbacks=Feedback.objects.all()
    coursefaculties=CourseFacultyLink.objects.all()
    class adding:
        design=0
        instructor=0
        tutorial=0
        exam=0
    class average:
        design=0
        instructor=0
        tutorial=0
        exam=0
    count=0
    for coursefaculty in coursefaculties:
        for feedback in feedbacks:
            adding=add(coursefaculty,feedback,adding)
            count=count+1
        if count != 0:
            average.design=adding.design/count
            average.instructor=adding.instructor/count
            average.tutorial=adding.tutorial/count
            average.exam=adding.exam/count
        coursefaculty.mid_design=average.design
        coursefaculty.mid_instructor=average.instructor
        coursefaculty.mid_tutorial=average.tutorial
        coursefaculty.mid_exam=average.exam
        count=0
        coursefaculty.save()
    return render_to_response("feedback/rating.html",{'coursefaculties':coursefaculties,},context_instance=RequestContext(request))



