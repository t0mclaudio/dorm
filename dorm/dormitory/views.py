from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
import datetime
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

# Create your views here.
@login_required
def index(request):
    is_manager = request.user.groups.filter(name="manager").exists()
    is_student = request.user.groups.filter(name="student").exists()
    is_admin= request.user.groups.filter(name="admin").exists()
    return render(request, 'index.html', {'is_manager':is_manager, 'is_student': is_student, 'is_admin': is_admin})

@login_required
def list_admins(request):
    admins = User.objects.filter(groups__name='admin')
    return render(request, 'admin_list.html', {"admins": admins})

@login_required
def add_admin(request):
    if request.method == "POST":
        form = UserForm(request.POST)
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
            g = Group.objects.get(name='admin')
            g.user_set.add(user)
            return render(request, 'index.html')
        else:
            return render(request, 'user_form.html', {'form': form} )
    else:
        form = UserForm()
    return render(request, 'user_form.html', {'form': form} )

def admin_profile(request):
    pass

def edit_admin_profile(request):
    pass

def delete_admin(request):
    pass

# Bunks
@login_required
def list_bunks(request):
    bunks = Bunk.objects.all()
    return render(request, 'bunks.html', {'bunks': bunks})

@login_required
def add_bunk(request):
    if request.method == "POST":
        form = BunkForm(request.POST)
        if form.is_valid():
            clean = form.clean()
            bunk = Bunk(code=clean['code'])
            bunk.save()
            return HttpResponseRedirect(reverse('view_bunks'))
        else:
            return render(request, 'bunkform.html', {'form': form})
    else:
        form = BunkForm()
        return render(request, 'bunkform.html', {'form': form})

@login_required
def bunk(request):
    pass

@login_required
def edit_bunk(request):
    pass

@login_required
def delete_bunk(request):
    pass

# Manager
@login_required
def list_managers(request):
    managers = User.objects.filter(groups__name='manager')
    return render(request, 'manager_list.html', {'managers': managers})

@login_required
def add_manager(request):
    if request.method == "POST":
        form = UserForm(request.POST)
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
            g = Group.objects.get(name='manager')
            g.user_set.add(user)
            return render(request, 'index.html')
        else:
            return render(request, 'user_form.html', {'form': form} )
    else:
        form = UserForm()
    return render(request, 'user_form.html', {'form': form} )



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
        form = UserForm(request.POST)
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
            g = Group.objects.get(name='manager')
            g.user_set.add(user)
            return render(request, 'index.html')
        else:
            return render(request, 'user_form.html', {'form': form} )
    else:
        form = UserForm()
    return render(request, 'user_form.html', {'form': form} )

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

@login_required
def logs(request):
    logs = Log.objects.all()
    return render(request, 'logs.html', {'logs':logs})
