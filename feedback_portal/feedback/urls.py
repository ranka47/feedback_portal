from django.conf.urls import url

from feedback import views

urlpatterns = [
        url(r'^$', views.login, name='index'),
        url('auth/$', views.auth_view),
        url('logout/$', views.logout),
        url('home/$', views.home),
        url('invalid/$', views.login),

        # url('endsem-feedback/$',views.endsem_feedback),

        url(r'^(?P<coursefaculty_id>\d+)/activate/submitted/$', views.activate_feedback),
        url(r'^(?P<coursefaculty_id>\d+)/activate/feedback/$', views.activate_feedback),

        url(r'^(?P<feedback_id>\d+)/(?P<coursefaculty_id>\d+)/midsem-fillfeedback/submit/$', views.midsem_fillfeedback),
        url(r'^(?P<feedback_id>\d+)/(?P<coursefaculty_id>\d+)/midsem-fillfeedback/$', views.midsem_fillfeedback),

        url(r'^(?P<feedback_id>\d+)/(?P<coursefaculty_id>\d+)/endsem-fillfeedback/submit/$', views.endsem_fillfeedback),
        url(r'^(?P<feedback_id>\d+)/(?P<coursefaculty_id>\d+)/endsem-fillfeedback/$', views.endsem_fillfeedback),

        url('midsem-feedback/$',views.midsem_feedback),
        url('endsem-feedback/$',views.endsem_feedback),
        
        url('comment/$', views.comment),
        url('rating/$', views.rating),
        # url(r'^(?P<task_id>\d+)/user/$',views.usertask_detail),
        url('new-post/$', views.new_post),
        url('submitted/$', views.new_post),

        url('edit-profile/$', views.edit_profile),

        url(r'^(?P<post_id>\d+)/post/$',views.detail),
        url(r'^(?P<post_id>\d+)/post/comment/$',views.post_comment),
        
        # url(r'^(?P<task_id>\d+)/pending/comment/$',views.pending_comment),
        
        # url('feedbacks-done/$', views.done_feedback),
        # url(r'^(?P<task_id>\d+)/done/$',views.done_detail),

        # url('new-template/$', views.new_template),
        # url('existing-template/$', views.existing_template),
        # url(r'^(?P<task_id>\d+)/accepted/$',views.accepted),
        # url(r'^(?P<task_id>\d+)/denied/$',views.denied),
        # url(r'^(?P<task_id>\d+)/delete/$',views.delete),
]