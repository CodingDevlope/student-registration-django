# Generated for the Student Registration practical.
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("full_name", models.CharField(max_length=100)),
                ("enrollment_no", models.CharField(max_length=30, unique=True)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("contact_number", models.CharField(max_length=15)),
                ("course", models.CharField(choices=[
                    ("Diploma Computer Engineering", "Diploma Computer Engineering"),
                    ("Diploma Information Technology", "Diploma Information Technology"),
                    ("BCA", "BCA"),
                    ("B.Sc. IT", "B.Sc. IT"),
                    ("Other", "Other"),
                ], max_length=60)),
                ("semester", models.PositiveSmallIntegerField(choices=[
                    (1, "Semester 1"), (2, "Semester 2"), (3, "Semester 3"),
                    (4, "Semester 4"), (5, "Semester 5"), (6, "Semester 6"),
                    (7, "Semester 7"), (8, "Semester 8"),
                ])),
                ("registered_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={"ordering": ["full_name"]},
        ),
    ]
