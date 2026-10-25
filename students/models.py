from django.db import models

class Student(models.Model):
    COURSE_CHOICES = [
        ("Diploma Computer Engineering", "Diploma Computer Engineering"),
        ("Diploma Information Technology", "Diploma Information Technology"),
        ("BCA", "BCA"),
        ("B.Sc. IT", "B.Sc. IT"),
        ("Other", "Other"),
    ]

    SEMESTER_CHOICES = [(i, f"Semester {i}") for i in range(1, 9)]

    full_name = models.CharField(max_length=100)
    enrollment_no = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=15)
    course = models.CharField(max_length=60, choices=COURSE_CHOICES)
    semester = models.PositiveSmallIntegerField(choices=SEMESTER_CHOICES)
    registered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["full_name"]

    def __str__(self):
        return f"{self.full_name} ({self.enrollment_no})"
