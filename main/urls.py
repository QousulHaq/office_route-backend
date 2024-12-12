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
    path('word_beginner', views.word_beginner, name='word_beginner')
    # Add paths for other pages like 'about', 'faqs', 'all_courses' as needed.
]
