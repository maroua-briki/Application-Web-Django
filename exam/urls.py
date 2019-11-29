from django.conf.urls import url

from . import views

app_name = "exam"

urlpatterns = [
    url(r'^index/$', views.home, name='index'),

    url(r'^create_exam/$', views.create_exam, name='create_exam'),

    url(r'^active_exams/$', views.active_exams, name='active_exams'),

    url(r'^(?P<pk>[0-9]+)/create_question/$', views.create_question, name='create_question'),

    # url(r'¨message/$', views.message, name='create_exam'),

    url(r'^(?P<exam_id>[0-9]+)/question_list/$', views.affich_question, name='question_list'),

    url(r'^(?P<question_id>[0-9]+)/delete_question/$', views.delete_question, name='delete'),

    url(r'^(?P<question_id>[0-9]+)/edit_ONE/$', views.edit_ONE, name='edit_ONE'),

    url(r'^(?P<question_id>[0-9]+)/edit_FREE/$', views.edit_FREE, name='edit_FREE'),

    url(r'^(?P<question_id>[0-9]+)/edit_MULTI/$', views.edit_MULTI, name='edit_MULTI'),

    # url(r'^(?P<exam_id>[0-9]+)/try_exam/$', views.try_exam, name='affich'),
    #
    # url(r'^(?P<exam_id>[0-9]+)/try_exam/(?P<question_id>[0-9]+)$', views.dbsave, name='try'),

    url(r'^(?P<exam_id>[0-9]+)/score/$', views.score, name='score'),

    url(r'^(?P<exam_id>[0-9]+)/try_exam/$', views.preparation, name='preparation'),

    url(r'^(?P<exam_id>[0-9]+)/try_exam/(?P<indice>[0-9]+)$', views.pass_exam, name='try'),

    url(r'^(?P<exam_id>[0-9]+)/save_respone/(?P<indice>[0-9]+)/$', views.save_response, name='save-reponse'),

    # url(r'^(?P<exam_id>[0-9]+)/save_respone/(?P<indice>[0-9]+)$', views.score, name='save-reponse'),

    url(r'^addlocal_stu/$', views.addlocal_stu, name='local_students'),

    url(r'^send/$', views.addstranger_stu, name='invitation'),

    url(r'^MYstudents/$', views.assignTO_exam, name='MYstudents'),

    url(r'^indexUSER/$', views.homeUSER, name='indexUSER'),

    url(r'^(?P<exam_id>[0-9]+)/try_examSTUD/$', views.preparationSTUD, name='preparationSTUD'),

    url(r'^(?P<exam_id>[0-9]+)/try_examSTUD/(?P<indice>[0-9]+)$', views.pass_examSTUD, name='trySTUD'),

    url(r'^(?P<exam_id>[0-9]+)/save_responeSTUD/(?P<indice>[0-9]+)/$', views.save_responseSTUD,
        name='save-reponseSTUD'),

    url(r'^(?P<exam_id>[0-9]+)/score_user/$', views.certif, name='scoreUSER'),

    url(r'^(?P<exam_id>[0-9]+)/certif/$', views.certif, name='certif'),

    url(r'^(?P<exam_id>[0-9]+)/correction/$', views.correction, name='correction'),

    url(r'^STUD_EXAMS/$', views.STUD_EXAMS, name='STUD_EXAMS'),

    url(r'^becomePROF/$', views.becomePROF, name='becomePROF'),

]
