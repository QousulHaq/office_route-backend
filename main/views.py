from django.shortcuts import redirect, get_object_or_404, render
from main.models import Course, Service, UserClass, Cart, Order, Payment, Quiz, UserQuiz, Certificate, UserProfileInfo, Question
from main.forms import UserForm, UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from django.utils.timezone import now
from reportlab.pdfgen import canvas


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
    cart = Cart.objects.get(user=request.user)
    total_price = sum(course.price for course in cart.courses.all())

    return render(request, 'main/all_course.html', context={"course" : course_data, 'cart': cart, 'total_price': total_price})

def all_course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    chapters = course.chapters.all().order_by('order')  # Mengambil chapter berdasarkan urutan
    mentor = course.mentor  # Mengambil mentor dari course

    context = {
        'course': course,
        'chapters': chapters,
        'mentor': mentor,
    }
    return render(request, 'main/word_beginner.html', context)

def my_course(request):
    user_classes = UserClass.objects.filter(user=request.user).select_related('course_id')
    courses = [user_class.course_id for user_class in user_classes]

    return render(request, 'main/my_course.html', context={"course" : courses})

# def my_course_detail(request, course_id):
#     course = get_object_or_404(Course, id=course_id)

#     # Ambil chapters dan materials terkait
#     chapters = course.chapters.order_by('order')  # Pastikan urutannya sesuai

#     context = {
#         'course': course,
#         'chapters': chapters,
#     }

#     return render(request, 'main/menu_belajar.html', context)

@login_required
def my_course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    # Ambil chapters terkait dengan urutan yang benar
    chapters = course.chapters.order_by('order')
    quizzes = []

    for chapter in chapters:
        quiz = chapter.quizzes.first()  # Mengambil quiz pertama dari chapter
        if quiz:
            # Cek apakah user sudah mengerjakan quiz
            user_quiz = UserQuiz.objects.filter(user=request.user, quiz=quiz).first()
            if user_quiz and user_quiz.is_completed:
                # Jika sudah dikerjakan, cek sertifikat
                certificate = Certificate.objects.filter(user=request.user, course_id=course).first()
                quizzes.append({
                    'quiz': quiz,
                    'status': 'completed',
                    'score': user_quiz.score,  # Menambahkan score ke dalam context
                    'certificate': certificate
                })
            else:
                quizzes.append({
                    'quiz': quiz,
                    'status': 'incomplete',
                    'score': None,  # Tidak ada score jika belum dikerjakan
                    'certificate': None
                })
        else:
            quizzes.append({
                'quiz': None,
                'status': 'no_quiz',
                'score': None,
                'certificate': None
            })

    context = {
        'course': course,
        'chapters': chapters,
        'quizzes': quizzes,  # Kirim data quiz ke template
    }

    return render(request, 'main/menu_belajar.html', context)


def menu_belajar(request):
    return render(request, 'main/menu_belajar.html')

# def quiz(request):
#     return render(request, 'main/quiz.html')

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

# # add cart bagian ini
# def add_to_cart(request, course_id):

#     if 'cart' not in request.session:
#         request.session['cart'] = []
    
#     course = get_object_or_404(Course, id=course_id)


#     if course_id not in request.session['cart']:
#         request.session['cart'].append(course_id)
#         request.session.modified = True  # Tandai session sebagai berubah
    
#     return redirect('main/all_course.html')

# def view_cart(request):
#     cart = request.session.get('cart', [])
#     return render(request, 'main/cart.html', {'cart': cart})


# def checkout(request):
#     # Logika untuk halaman checkout
#     return render(request, 'main/checkout.html')  # Pastikan Anda memiliki file checkout.html

def add_to_cart(request, course_id):
    if request.user.is_authenticated:
        course = get_object_or_404(Course, id=course_id)
        cart, _ = Cart.objects.get_or_create(user=request.user)
        cart.courses.add(course)

        messages.success(request, f'{course.title} has been added to your cart.')

        return redirect('all_course_detail', course_id=course.id)
    
    else:
        return redirect('login')

def checkout(request):
    cart = Cart.objects.get(user=request.user)
    total_price = sum(course.price for course in cart.courses.all())
    return render(request, 'checkout.html', {'cart': cart, 'total_price': total_price})

def create_order(request):
    cart = Cart.objects.get(user=request.user)
    total_price = sum(course.price for course in cart.courses.all())

    # Cek apakah sudah ada order pending
    order, created = Order.objects.get_or_create(
        user=request.user,
        status='Pending',
        defaults={'total_price': total_price}
    )

    if created:
        order.courses.set(cart.courses.all())  # Tambahkan courses ke order baru
        cart.courses.clear()  # Kosongkan keranjang jika order baru dibuat

    return render(request, 'main/checkout.html', {'order': order})

def upload_payment_proof(request, order_id):
    if request.method == 'POST':
        order = get_object_or_404(Order, id=order_id, user=request.user)
        payment_proof = request.FILES.get('payment_proof')

        if payment_proof:
            order.payment_proof = payment_proof
            order.status = 'Waiting Verification'
            order.save()
            messages.success(request, 'Bukti pembayaran berhasil diunggah. Menunggu verifikasi admin.')
        else:
            messages.error(request, 'Harap unggah file bukti pembayaran.')

    return redirect('payment_history')

def payment_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'main/payment_history.html', {'orders': orders})

def update_order(request, order_id):
    if request.method == "POST":
        # Ambil data order
        order = Order.objects.get(id=order_id, user=request.user)

        # Ambil data dari form
        payment_method = request.POST.get('payment_method')
        payment_proof = request.FILES.get('payment_proof')

        # Perbarui order
        order.payment_method = payment_method
        if payment_proof:
            order.payment_proof = payment_proof
        order.status = 'Pending'  # Ubah status order
        order.save()

        # Redirect ke halaman riwayat pembayaran
        return redirect('payment_history')
    return HttpResponse("Invalid request", status=400)

@login_required
def take_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    user_quiz, created = UserQuiz.objects.get_or_create(user=request.user, quiz=quiz)

    course_id_redirect = quiz.chapter_id.course_id.id

    # Jika kuis sudah selesai
    if user_quiz.is_completed:
        messages.warning(request, "You have already completed this quiz.")
        return redirect('quiz_list')  # Redirect ke halaman daftar kuis

    if request.method == 'POST':
        # Proses jawaban dari pengguna
        total_questions = quiz.questions.count()
        correct_answers = 0

        for question in quiz.questions.all():
            user_answer = request.POST.get(f'question_{question.id}')
            if user_answer and user_answer == question.correct_answer:
                correct_answers += 1

        # Hitung skor
        score = (correct_answers / total_questions) * 100
        user_quiz.score = score
        user_quiz.is_completed = True
        user_quiz.completed_at = now()
        user_quiz.save()

        # Beri EXP dan update level
        exp_gained = int(score // 10)  # 10% dari skor sebagai EXP
        profile = UserProfileInfo.objects.get(user=request.user)
        profile.exp += exp_gained
        if profile.exp >= 100:  # Setiap 100 EXP naik 1 level
            profile.exp -= 100
            profile.level += 1
        profile.save()

        # Beri sertifikat
        Certificate.objects.create(
            user=request.user,
            course_id=quiz.chapter_id.course_id,
            certificate_url=f"https://example.com/certificates/{quiz_id}_{request.user.id}.pdf"
        )

        messages.success(request, f"Quiz completed! Your score: {score:.2f}. Certificate issued.")
        return redirect('my_course_detail', course_id=course_id_redirect)

    # Render halaman kuis
    return render(request, 'main/quiz.html', {'quiz': quiz, 'questions': quiz.questions.all(),})

def generate_certificate(request, certificate_id):
    certificate = get_object_or_404(Certificate, id=certificate_id)

    # Create a PDF response
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="certificate_{certificate.id}.pdf"'

    # Generate PDF
    pdf = canvas.Canvas(response)
    pdf.drawString(100, 750, f"Certificate of Completion")
    pdf.drawString(100, 730, f"This certifies that {certificate.user.username}")
    pdf.drawString(100, 710, f"has successfully completed the course: {certificate.course_id.title}")
    pdf.drawString(100, 690, f"Issued on: {certificate.issued_at.strftime('%Y-%m-%d')}")
    pdf.save()

    return response




