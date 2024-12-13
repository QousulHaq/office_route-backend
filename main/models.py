from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Mentor(models.Model):
    name = models.CharField(max_length=255)
    experience = models.TextField()
    skills = models.JSONField()  # Store skills as a JSON array
    mentor_profile = models.ImageField(upload_to='mentors/', blank=True, null=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    image = models.ImageField(upload_to='courses/')
    title = models.CharField(max_length=200)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE, related_name="courses", null=True, blank=True)
    description = models.TextField()
    rating = models.PositiveSmallIntegerField()
    price = models.IntegerField()
    category = models.CharField(max_length=50, choices=[('Word', 'Word'), ('Excel', 'Excel'), ('PowerPoint', 'PowerPoint')], default='Word')
    is_free = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    @property
    def total_duration(self):
        return sum(chapter.duration for chapter in self.chapters.all())


class Service(models.Model):
    icon = models.ImageField(upload_to='services/')
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class UserProfileInfo(models.Model):
    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Add any additional attributes you want
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    # new attribute
    level = models.IntegerField(default=1)
    rank = models.CharField(max_length=50, default="Beginner")
    exp = models.IntegerField(default=0)

    # Create __str__ method to override the default one
    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username

class Chapter(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="chapters")
    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField()  # To maintain the order of chapters
    duration = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.title
    
# 3. Material Model
class Material(models.Model):
    chapter_id = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name="materials")
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)  # Could be a URL or textual content
    youtube_url = models.TextField(null=True, blank=True)  # Could be a URL or textual content
    order = models.PositiveIntegerField()

    def __str__(self):
        return self.title

# 4. Quiz Model
class Quiz(models.Model):
    chapter_id = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name="quizzes")
    title = models.CharField(max_length=255)
    total_questions = models.PositiveIntegerField()

    def __str__(self):
        return self.title

# 5. Question Model
class Question(models.Model):
    quiz_id = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")
    question_text = models.TextField()
    options = models.JSONField()  # Store options as a JSON object
    correct_answer = models.CharField(max_length=255)

# 6. UserClass Model
class UserClass(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="enrolled_classes")
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="enrollments")
    progress = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    completed_at = models.DateTimeField(null=True, blank=True)

# 7. UserQuiz Model
class UserQuiz(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="quizzes")
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="attempts")
    score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)  # Pastikan flag penyelesaian kuis

# 8. Certificate Model
class Certificate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="certificates")
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="certificates")
    issued_at = models.DateTimeField(auto_now_add=True)
    certificate_url = models.URLField()

    class Meta:
        unique_together = ('user', 'course_id')

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="cart")
    courses = models.ManyToManyField('Course', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    courses = models.ManyToManyField('Course')
    total_price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[
        ('Pending', 'Pending'),
        ('Waiting Verification', 'Waiting Verification'),
        ('Paid', 'Paid'),
        ('Failed', 'Failed'),
    ], default='Pending')
    payment_method = models.CharField(max_length=50, null=True, blank=True)
    payment_proof = models.FileField(upload_to='payment_proofs/', null=True, blank=True)

class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name="payment")
    payment_method = models.CharField(max_length=50, choices=[('Bank Transfer', 'Bank Transfer'), ('E-Wallet', 'E-Wallet'), ('Credit Card', 'Credit Card')])
    payment_proof = models.ImageField(upload_to='payment_proofs/', blank=True, null=True)
    uploaded_at = models.DateTimeField(default=now)
    verified = models.BooleanField(default=False)