from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, 'main/about.html')

def index(request):
    return render(request, 'main/index.html')

def signup(request):
    return render(request, 'main/signup.html')

def login(request):
    return render(request, 'main/login.html')

def faqs(request):
    return render(request, 'main/faqs.html')

def all_course(request):
    return render(request, 'main/all_course.html')