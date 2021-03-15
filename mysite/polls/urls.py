from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('student', views.student_detail),
    url(r'^signup/$', views.signup, name='signup'),

]