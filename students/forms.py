from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            "full_name", "enrollment_no", "email",
            "contact_number", "course", "semester",
        ]
        widgets = {
            "full_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter full name"}),
            "enrollment_no": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter enrollment number"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "student@example.com"}),
            "contact_number": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter contact number"}),
            "course": forms.Select(attrs={"class": "form-select"}),
            "semester": forms.Select(attrs={"class": "form-select"}),
        }

    def clean_contact_number(self):
        number = self.cleaned_data["contact_number"].strip()
        digits = "".join(ch for ch in number if ch.isdigit())
        if len(digits) < 10 or len(digits) > 15:
            raise forms.ValidationError("Enter a valid contact number containing 10 to 15 digits.")
        return number
