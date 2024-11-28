from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('faqs', views.faqs, name='faqs'),
    path('all_course', views.all_course, name='all_course'),
]
