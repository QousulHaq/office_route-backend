from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('faqs', views.faqs, name='faqs'),
    path('all_course', views.all_course, name='all_course'),
    path('logout/', views.user_logout, name='logout'),
    path('cart/', views.cart_view, name='cart'),
    path('pembayaran/', views.pembayaran_view, name='pembayaran'),
    path('menu_belajar/', views.menu_belajar, name='menu_belajar'),
    path('quiz/', views.quiz, name='quiz'),
    path('add_to_cart/<int:course_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('word_beginner', views.word_beginner, name='word_beginner'),
    path('word_intermediate', views.word_intermediate, name='word_intermediate'),
    path('word_advanced', views.word_advanced, name='word_advanced'),
    path('excel_beginner', views.excel_beginner, name='excel_beginner'),
    path('excel_intermediate', views.excel_intermediate, name='excel_intermediate'),
    path('excel_advanced', views.excel_advanced, name='excel_advanced'),
    path('ppt_beginner', views.ppt_beginner, name='ppt_beginner'),
    path('ppt_intermediate', views.ppt_intermediate, name='ppt_intermediate'),
    path('ppt_advanced', views.ppt_advanced, name='ppt_advanced'),
    # Add paths for other pages like 'about', 'faqs', 'all_courses' as needed.
]
