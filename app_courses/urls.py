from django.urls import path
from . import views

urlpatterns = [
    path('',views.courses,name='Courses'),
    #Dynamic Link for Courses
    path('<str:course_id>',views.course,name='Course')
]