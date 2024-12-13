from django.contrib import admin
from django.utils.html import format_html
from .models import Course, Service, UserProfileInfo, Material, Quiz, Question, UserClass, UserQuiz, Certificate, Chapter, Mentor, Cart, Order, Payment

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
admin.site.register(Cart)
admin.site.register(Payment)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_price', 'status', 'payment_proof_link')
    list_filter = ('status',)
    actions = ['mark_as_paid', 'mark_as_rejected']

    def payment_proof_link(self, obj):
        if obj.payment_proof:
            return format_html('<a href="{}" target="_blank">Lihat Bukti</a>', obj.payment_proof.url)
        return "Tidak ada bukti"
    payment_proof_link.short_description = 'Bukti Pembayaran'

    def mark_as_paid(self, request, queryset):
        for order in queryset:
            order.status = 'Paid'
            order.save()

            # Menambahkan course yang dibeli ke UserClass
            for course in order.courses.all():
                UserClass.objects.create(user=order.user, course_id=course, progress=0.0)

        self.message_user(request, "Order berhasil ditandai sebagai 'Paid' dan courses ditambahkan ke UserClass.")

    def mark_as_rejected(self, request, queryset):
        for order in queryset:
            order.status = 'Failed'
            order.save()

            # Menghapus course yang dipesan dari UserClass
            for course in order.courses.all():
                UserClass.objects.filter(user=order.user, course_id=course).delete()

        self.message_user(request, "Order berhasil ditandai sebagai 'Failed' dan courses dihapus dari UserClass.")

    mark_as_paid.short_description = "Tandai sebagai Paid"
    mark_as_rejected.short_description = "Tandai sebagai Failed"

# Register model Order dengan custom admin
admin.site.register(Order, OrderAdmin)
