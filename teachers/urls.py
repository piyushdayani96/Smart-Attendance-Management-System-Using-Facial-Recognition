from django.conf.urls import url
from django.conf import settings
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.views.static import serve
urlpatterns=[
    url(r'^$',views.home,name='home'),
url(r'^capture',views.capture,name='capture'),
url(r'^indexes',views.indexes,name='indexes'),
url(r'^face_detect',views.face_detect,name='face_detect'),
url(r'^attend',views.attend,name='attend'),
url(r'^viewstudentgroup',views.viewstudentgroup,name='viewstudentgroup'),
url(r'^createstudentgroup/(?P<id>\d+)$',views.createstudentgroup,name='createstudentgroup'),
url(r'^savestudentgroup',views.savestudentgroup,name='savestudentgroup'),
url(r'^viewattendance',views.viewattendance,name='viewattendance'),
url(r'^download',views.download,name='download'),
url(r'^awesome_method',views.awesome_method,name='awesome_method'),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)