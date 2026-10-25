from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("full_name", "enrollment_no", "email", "course", "semester", "registered_at")
    search_fields = ("full_name", "enrollment_no", "email")
    list_filter = ("course", "semester")
