from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from .forms import StudentForm
from .models import Student

def student_list(request):
    query = request.GET.get("q", "").strip()
    students = Student.objects.all()
    if query:
        students = students.filter(
            Q(full_name__icontains=query)
            | Q(enrollment_no__icontains=query)
            | Q(email__icontains=query)
            | Q(course__icontains=query)
        )
    return render(request, "students/student_list.html", {
        "students": students,
        "query": query,
        "student_count": Student.objects.count(),
    })

def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student registered successfully.")
            return redirect("student_list")
    else:
        form = StudentForm()
    return render(request, "students/student_form.html", {
        "form": form,
        "page_title": "Register Student",
        "button_text": "Register Student",
    })

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student details updated successfully.")
            return redirect("student_list")
    else:
        form = StudentForm(instance=student)
    return render(request, "students/student_form.html", {
        "form": form,
        "page_title": "Edit Student",
        "button_text": "Save Changes",
        "student": student,
    })

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        messages.success(request, "Student record deleted.")
        return redirect("student_list")
    return render(request, "students/student_confirm_delete.html", {"student": student})
