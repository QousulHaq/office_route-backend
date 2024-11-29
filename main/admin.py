from django.contrib import admin
from .models import Course, Service, UserProfileInfo

# Register your models here.

admin.site.register(Course)
admin.site.register(Service)
admin.site.register(UserProfileInfo)