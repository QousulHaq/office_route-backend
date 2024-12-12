from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse
from main.models import Course, Service
from main.forms import UserForm, UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def about(request):
    return render(request, 'main/about.html')

def index(request):
    course_data = Course.objects.all()
    service_data = Service.objects.all()
    return render(request, 'main/index.html', context={"course" : course_data, "service" : service_data})

@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def signup(request):
    registered = False  # Beri nilai awal pada variabel

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)  # Hash the password
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user  # OneToOne relationship

            if "profile_pic" in request.FILES:
                profile.profile_pic = request.FILES["profile_pic"]

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    # Masukkan semua variabel ke dalam konteks template
    formdict = {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}
    return render(request, 'main/signup.html', formdict)


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")  # Get from login.html
        password = request.POST.get("password")  # Get from login.html

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
            else:
                return HttpResponse("Account not active")
        else:
            print("Someone tried to login and failed")
            print(f"Username: {username} and password: {password}")
            return HttpResponse("Invalid login details supplied!")
    else:
        return render(request, "main/login.html", {})

def faqs(request):
    return render(request, 'main/faqs.html')

def cart_view(request):
    return render(request, 'main/cart.html')

def pembayaran_view(request):
    return render(request, 'main/pembayaran.html')

def all_course(request):
    course_data = Course.objects.all()
    return render(request, 'main/all_course.html', context={"course" : course_data})

def menu_belajar(request):
    return render(request, 'main/menu_belajar.html')

def quiz(request):
    return render(request, 'main/quiz.html')

def word_beginner(request):
    return render(request, 'main/word_beginner.html')

def word_intermediate(request):
    return render(request, 'main/word_intermediate.html')

def word_advanced(request):
    return render(request, 'main/word_advanced.html')

def excel_beginner(request):
    return render(request, 'main/excel_beginner.html')

def excel_intermediate(request):
    return render(request, 'main/excel_intermediate.html')

def excel_advanced(request):
    return render(request, 'main/excel_advanced.html')

def ppt_beginner(request):
    return render(request, 'main/ppt_beginner.html')

def ppt_intermediate(request):
    return render(request, 'main/ppt_intermediate.html')

def ppt_advanced(request):
    return render(request, 'main/ppt_advanced.html')

# add cart bagian ini
def add_to_cart(request, course_id):

    if 'cart' not in request.session:
        request.session['cart'] = []
    
    course = get_object_or_404(Course, id=course_id)


    if course_id not in request.session['cart']:
        request.session['cart'].append(course_id)
        request.session.modified = True  # Tandai session sebagai berubah
    
    return redirect('main/all_course.html')

def view_cart(request):
    cart = request.session.get('cart', [])
    return render(request, 'main/cart.html', {'cart': cart})

