from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
import datetime

# Create your views here.
@login_required
def index(request):
    return render(request, 'index.html')


@login_required
def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            clean = form.clean()
            user = User(
                username = clean['username'],
                first_name = clean['first_name'],
                last_name = clean['last_name'],
                email = clean['email'],
                password = clean['password'],
            )
            user.save()
            user.set_password(user.password)
            user.save()
            g = Group.objects.get(name='student')
            g.user_set.add(user)
            bunk = Bunk.objects.get(code=clean['bunk'])
            student = Student(
                user=user,
                course=clean['course'],
                contact_no=clean['contact_no'],
                birth_date=clean['birth_date'],
                mother_name=clean['mother_name'],
                mother_contact=clean['mother_contact'],
                father_name=clean['father_name'],
                father_contact=clean['father_contact'],
                guardian_name=clean['guardian_name'],
                guardian_contact=clean['guardian_contact'],
                bunk = bunk,
                )
            student.save()
            return render(request, 'index.html')
        else:
            return render(request, 'student_form.html', {'form': form} )
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form} )

@login_required
def add_manager(request):
    if request.method == "POST":
        form = DManagerForm(request.POST)
        if form.is_valid():
            clean = form.clean()
            user = User(
                username = clean['username'],
                first_name = clean['first_name'],
                last_name = clean['last_name'],
                email = clean['email'],
                password = clean['password'],
            )
            user.save()
            g = Group.objects.get(name='manager')
            g.user_set.add(user)
            return render(request, 'index.html')
        else:
            return render(request, 'Dmanager_form.html', {'form': form} )
    else:
        form = DManagerForm()
    return render(request, 'Dmanager_form.html', {'form': form} )

@login_required
def students(request):
    students = Student.objects.all()
    return render(request, 'students.html', {'students': students})

@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    profile = Student.objects.get(user=user)
    return render(request, 'profile.html', {'profile': profile})

@login_required
def student_logs(request, username):
    user = User.objects.get(username=username)
    student = Student.objects.get(user=user)
    logs = Log.objects.filter(student=student)
    return render(request, 'student_logs.html', {'logs': logs})

@login_required
def student_in(request, username):
    if request.method == "POST":
        user = User.objects.get(username=username)
        student = Student.objects.get(user=user)
        log = Log(
            student = student,
            log_type = "In",
            destination = "",
            datetime = datetime.datetime.now()
        )
        log.save()
        return render(request, 'index.html')
    return render(request, 's_login.html')

@login_required
def student_out(request, username):
    if request.method == "POST":
        user = User.objects.get(username=username)
        student = Student.objects.get(user=user)
        log = Log(
            student = student,
            log_type = "Out",
            destination = request.POST['destination'],
            datetime = datetime.datetime.now()
        )
        log.save()
        return render(request, 'index.html')
    return render(request, 's_logout.html')
