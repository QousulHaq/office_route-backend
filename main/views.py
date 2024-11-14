from django.shortcuts import render
from django.http import HttpResponse
from main.models import Course

# Create your views here.
def about(request):
    return render(request, 'main/about.html')

def index(request):
    course_data = Course.objects.all()
    return render(request, 'main/index.html', context={"course" : course_data})

def signup(request):
    return render(request, 'main/signup.html')

def login(request):
    return render(request, 'main/login.html')

def faqs(request):
    return render(request, 'main/faqs.html')

def all_course(request):
    course_data = Course.objects.all()
    return render(request, 'main/all_course.html', context={"course" : course_data})