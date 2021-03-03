from django.conf.urls import url
from . import views

urlpatterns=[
url(r'^userzone',views.userzone,name='userzone'),
url(r'^discussion', views.discussion, name='discussion'),
url(r'^searchsolution', views.searchsolution, name='searchsolution'),
url(r'^complainlog', views.complainlog, name='complainlog'),
url(r'^changepassword', views.changepassword, name='changepassword'),
url(r'^postquestion', views.postquestion, name='postquestion'),
url(r'^answer/(?P<qid>\d+)$', views.answer, name='answer'),
url(r'^postanswer', views.postanswer, name='postanswer'),
url(r'^viewanswer/(?P<qid>\d+)$', views.viewanswer, name='viewanswer'),
url(r'^changepwd', views.changepwd, name='changepwd'),
url(r'^savecomplain', views.savecomplain, name='savecomplain'),
url(r'^answer/(?P<qid>\d+)$',views.answer,name='answer'),
url(r'^postanswer',views.postanswer,name='postanswer'),
url(r'^viewanswer/(?P<qid>\d+)$',views.viewanswer,name='viewanswer'),
]