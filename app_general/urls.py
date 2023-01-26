from django.urls import path
from . import views

#Map links and views
urlpatterns = [
    path('',views.home,name='Home'),
    path('about',views.about,name='About')
]