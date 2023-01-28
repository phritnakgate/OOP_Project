from django.urls import path
from . import views

urlpatterns = [
    path('',views.courses,name='Courses'),
    #Dynamic Link for Courses
    path('<int:course_id>',views.course,name='Course')
]