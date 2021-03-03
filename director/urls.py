from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^$',views.direchome,name='direchome'),
    url(r'^createtable',views.createtable,name='createtable'),
    url(r'^savetable',views.savetable,name='savetable'),
    url(r'^deletedepartment/(?P<id>\d+)$',views.deletedepartment,name='deletedepartment'),
    url(r'^createsubject',views.createsubject,name='createsubject'),
    url(r'^showsubject/(?P<id>\d+)$',views.showsubject,name='showsubject'),
    url(r'^savesubject',views.savesubject,name='savesubject'),

]