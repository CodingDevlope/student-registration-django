# Student Registration Web Application

A beginner-friendly Django CRUD practical adapted from the Book Management structure in Practical 15. It uses Django, SQLite, HTML, CSS and Bootstrap 5.

## Features
- Register student records
- List and search students
- Edit student details
- Delete records with a confirmation page
- SQLite database and Django admin
- Responsive Bootstrap interface

## Student fields
Full name, enrollment number, email, contact number, course and semester. Enrollment number and email must be unique.

## 1. Requirements
- Python 3.10+
- Git
- A GitHub account
- VS Code (recommended)

## 2. Run locally on Windows

Open a terminal in this project folder:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py makemigrations students
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/

If PowerShell blocks activation, use Command Prompt and run:
```bat
.venv\Scripts\activate.bat
```

## 3. Test the practical
1. Open the home page.
2. Click **Register Student** and enter valid details.
3. Confirm the student appears in the directory.
4. Use Search to find a student by name, enrollment number, email or course.
5. Click Edit and save a change.
6. Click Delete and confirm.
7. Optional admin: run `python manage.py createsuperuser`, then visit `/admin/`.

## 4. Upload the project to GitHub

Create a new **empty** repository on GitHub, for example `student-registration-django`. Do not add a README or license on GitHub if you already have this project locally.

Run these commands from the project folder (replace the URL with your own repository URL):

```bash
git init
git add .
git commit -m "Create Django student registration app"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/student-registration-django.git
git push -u origin main
```

The `.gitignore` file excludes the local SQLite database and virtual environment. Do not commit passwords, API keys, or private student information.

For later code updates:
```bash
git add .
git commit -m "Update student registration app"
git push
```

## 5. Deploy on PythonAnywhere using GitHub

GitHub stores the code; PythonAnywhere runs the Django application. GitHub Pages alone cannot host Django/Python server code.

1. Create/sign in to a PythonAnywhere account.
2. Open **Consoles** and start a Bash console.
3. Clone your GitHub repository (replace the URL):
   ```bash
   git clone https://github.com/YOUR-USERNAME/student-registration-django.git
   cd student-registration-django
   ```
4. Create a virtual environment. Use a Python version supported by your PythonAnywhere account:
   ```bash
   python3.12 -m venv ~/.virtualenvs/student-registration
   source ~/.virtualenvs/student-registration/bin/activate
   pip install -r requirements.txt
   ```
   If `python3.12` is unavailable, select an available supported Python version and use the same version when creating the Web app.
5. In PythonAnywhere **Web** tab, create a new web app, choose **Manual configuration**, and select the same Python version.
6. Set the virtualenv field to:
   ` /home/YOUR-USERNAME/.virtualenvs/student-registration `
   Replace `YOUR-USERNAME` with your actual PythonAnywhere username.
7. Edit the WSGI configuration file linked on the Web tab. Replace its application code with the following, changing the username and repository folder if yours differs:
   ```python
   import os
   import sys

   project_home = '/home/YOUR-USERNAME/student-registration-django'
   if project_home not in sys.path:
       sys.path.insert(0, project_home)

   os.environ['DJANGO_SETTINGS_MODULE'] = 'student_project.settings'
   os.environ['DJANGO_DEBUG'] = 'False'
   os.environ['DJANGO_ALLOWED_HOSTS'] = 'YOUR-USERNAME.pythonanywhere.com'
   os.environ['DJANGO_SECRET_KEY'] = 'replace-this-with-a-long-random-secret'

   from django.core.wsgi import get_wsgi_application
   application = get_wsgi_application()
   ```
   Use a unique secret key and keep it private. Do not commit it to GitHub. Prefer PythonAnywhere environment-variable configuration where available.
8. In the Bash console, activate the virtual environment and run:
   ```bash
   cd ~/student-registration-django
   source ~/.virtualenvs/student-registration/bin/activate
   python manage.py check
   python manage.py migrate
   python manage.py collectstatic --noinput
   ```
9. In the PythonAnywhere Web tab, set the static files mapping:
   - URL: `/static/`
   - Directory: `/home/YOUR-USERNAME/student-registration-django/staticfiles`
10. Click **Reload** in the Web tab and open:
    `https://YOUR-USERNAME.pythonanywhere.com/`

### Update the deployed site after pushing to GitHub

In a PythonAnywhere Bash console:
```bash
cd ~/student-registration-django
git pull
source ~/.virtualenvs/student-registration/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
```
Then click **Reload** in the Web tab.

## 6. Important deployment notes
- Replace every `YOUR-USERNAME` placeholder with your real username.
- Keep `DEBUG=False` in production.
- The SQLite database is stored on PythonAnywhere and is not synchronized by GitHub. Back it up separately.
- Free-hosting features and console commands can vary by account; follow the current PythonAnywhere dashboard instructions if labels differ.
- This is a student-record CRUD demo, not a full authenticated public enrollment system. Before collecting real student data, add login/permissions, privacy protections, backups and appropriate access controls.

## Practical write-up

**Aim:** To develop a Student Registration web application using Django and SQLite, perform CRUD operations, and publish the source code to GitHub before deploying the application on PythonAnywhere.

**Software requirements:** Python, Django, SQLite, HTML, CSS, Bootstrap 5, VS Code, Git, GitHub and PythonAnywhere.

**Theory:** Django is a Python web framework that follows the Model-View-Template (MVT) pattern. The Student model stores registration data in SQLite. Django forms validate the submitted fields, views process create/read/update/delete operations, templates display the interface, and Bootstrap styles the pages.

**Procedure:** Create the Django project and students app; register the app in `INSTALLED_APPS`; define the Student model and ModelForm; implement CRUD views and URL routes; create templates; migrate the database; test locally; push the project to GitHub; clone it on PythonAnywhere; configure the virtual environment and WSGI file; migrate and collect static files; reload and test the live site.

**Expected output:** Student directory, student registration form, edit student form, delete confirmation page, and a live deployed application URL.
