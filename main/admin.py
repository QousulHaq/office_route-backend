from django.contrib import admin
from .models import Course, Service, UserProfileInfo, Material, Quiz, Question, UserClass, UserQuiz, Certificate, Chapter, Mentor

# Register your models here.

admin.site.register(Course)
admin.site.register(Service)
admin.site.register(UserProfileInfo)
admin.site.register(Material)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(UserClass)
admin.site.register(UserQuiz)
admin.site.register(Certificate)
admin.site.register(Chapter)
admin.site.register(Mentor)