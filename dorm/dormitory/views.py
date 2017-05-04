from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
import datetime
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages

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
            try:
                user.save()
                user.set_password(user.password)
                user.save()
                g = Group.objects.get(name='admin')
                g.user_set.add(user)
            except:
                messages.warning(request, "An error occured while saving. Make sure username and email address are unique")
                return HttpResponseRedirect(reverse('list_admins'))
            messages.success(request, "A new admin has been created.")
            return HttpResponseRedirect(reverse('list_admins'))
        else:
            messages.warning(request, "Error on form values.")
            return render(request, 'user_form.html', {'form': form} )
    else:
        form = UserForm()
    return render(request, 'user_form.html', {'form': form} )

def admin_profile(request, username):
    profile = User.objects.get(username=username)
    return render(request, 'admin_profile.html', {'profile': profile} )

def edit_admin_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            clean = form.clean()
            user.username = clean['username']
            user.first_name = clean['first_name']
            user.last_name = clean['last_name']
            user.email = clean['email']
            user.set_password(clean['password'])
            try:
                user.save()
            except:
                messages.warning(request, "An error occured while saving. Make sure email address are unique")
                return HttpResponseRedirect(reverse('list_admins'))
            messages.success(request, "Admin profile updated.")
            return HttpResponseRedirect(reverse('list_admins'))
        else:
            messages.warning(request, "Error on form values.")
            return render(request, 'user_form.html', {'form': form})
    else:
        form = UserForm(initial={
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'password': user.password
        })
        form.fields['username'].widget.attrs['readonly'] = True
    return render(request, 'user_form.html', {'form': form})


def delete_admin(request, username):
    user = User.objects.get(username=username)
    user.delete()
    messages.success(request, "Success: An admin has been removed")
    return HttpResponseRedirect(reverse('list_admins'))

# Bunks
@login_required
def list_bunks(request):
    bunks = Bunk.objects.all()
    return render(request, 'bunk_list.html', {'bunks': bunks})

@login_required
def add_bunk(request):
    if request.method == "POST":
        form = BunkForm(request.POST)
        if form.is_valid():
            clean = form.clean()
            bunk = Bunk(code=clean['code'])
            try:
                bunk.save()
            except:
                messages.warning(request, "An error occured while saving. Make sure code is unique")
                return HttpResponseRedirect(reverse('list_bunks'))
            messages.success(request, "Success: A bunk bed has been added")
            return HttpResponseRedirect(reverse('list_bunks'))
        else:
            return render(request, 'bunkform.html', {'form': form})
    else:
        form = BunkForm()
        return render(request, 'bunkform.html', {'form': form})

@login_required
def bunk(request, id):
    bunk = Bunk.objects.get(id=id)
    return render(request, 'bunk.html', {'bunk': bunk} )

@login_required
def edit_bunk(request, id):
    bunk = Bunk.objects.get(id=id)
    if request.method == "POST":
        form = BunkForm(request.POST)
        if form.is_valid():
            clean = form.clean()
            bunk.code = clean['code']
            try:
                bunk.save()
            except:
                messages.warning(request, "An error occured while saving. Make sure code is unique")
                return HttpResponseRedirect(reverse('list_bunks'))
            messages.success(request, "Success: A bunk bed has been edited")
            return HttpResponseRedirect(reverse('list_bunks'))
        else:
            messages.warning(request, "An error in the form fields")
            return render(request, 'bunkform.html', {'form': form})
    else:
        form = BunkForm(initial={'code': bunk.code})
    return render(request, 'bunkform.html', {'form': form})

@login_required
def delete_bunk(request, id):
    bunk = Bunk.objects.get(id=id)
    bunk.delete()
    messages.success(request, "Success: A bunk bed has been removed")
    return HttpResponseRedirect(reverse('list_bunks'))

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
            try:
                user.save()
                user.set_password(user.password)
                user.save()
                g = Group.objects.get(name='manager')
                g.user_set.add(user)
                messages.success(request, "A new manager has been created.")
            except:
                messages.warning(request, "An error occured while saving. Make sure username and email address are unique")
            return HttpResponseRedirect(reverse('list_managers'))
        else:
            messages.warning(request, "Error on form values.")
            return render(request, 'user_form.html', {'form': form} )
    else:
        form = UserForm()
    return render(request, 'user_form.html', {'form': form} )

@login_required
def manager_profile(request, username):
    profile = User.objects.get(username=username)
    return render(request, 'manager_profile.html', {'profile': profile} )

@login_required
def edit_manager_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            clean = form.clean()
            user.username = clean['username']
            user.first_name = clean['first_name']
            user.last_name = clean['last_name']
            user.email = clean['email']
            user.set_password(clean['password'])
            try:
                user.save()
                messages.success(request, "Success: A manager profile has been edited")
            except:
                messages.warning(request, "An error occured while saving.")
            return HttpResponseRedirect(reverse('list_managers'))
        else:
            messages.warning(request, "An error in the form fields")
            return render(request, 'user_form.html', {'form': form})
    else:
        form = UserForm(initial={
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'password': user.password
        })
        form.fields['username'].widget.attrs['readonly'] = True
    return render(request, 'user_form.html', {'form': form})

@login_required
def delete_manager(request, username):
    user = User.objects.get(username=username)
    user.delete()
    messages.success(request, "Success: A manager has been removed")
    return HttpResponseRedirect(reverse('list_managers'))

@login_required
def list_students(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

@login_required
def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        form.fields['bunk'].choices=Bunk.objects.get_available()
        if form.is_valid():
            clean = form.clean()
            user = User(
                username = clean['username'],
                first_name = clean['first_name'],
                last_name = clean['last_name'],
                email = clean['email'],
                password = clean['password'],
            )
            try:
                user.save()
                user.set_password(user.password)
                user.save()
                g = Group.objects.get(name='student')
                g.user_set.add(user)
                bunk = Bunk.objects.get(id=clean['bunk'])
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
                messages.success(request, "Success: A student profile has been edited")
            except:
                messages.warning(request, "An error occured while saving.")
            return HttpResponseRedirect(reverse('list_students'))
        else:
            messages.warning(request, "An error occured while saving.")
            return render(request, 'student_form.html', {'form': form} )
    else:
        form = StudentForm()
        form.fields['bunk'].choices=Bunk.objects.get_available()
    return render(request, 'student_form.html', {'form': form} )

@login_required
def student_profile(request, username):
    user = User.objects.get(username=username)
    profile = Student.objects.get(user=user)
    return render(request, 'student_profile.html', {'profile': profile})

@login_required
def edit_student_profile(request, username):
    user = User.objects.get(username=username)
    profile = Student.objects.get(user=user)
    if request.method == "POST":
        form = StudentForm(request.POST)
        form.fields['bunk'].choices=Bunk.objects.get_available2(profile.bunk.id)
        if form.is_valid():
            try:
                clean = form.clean()
                bunk = Bunk.objects.get(id=clean['bunk'])
                user.username = clean['username']
                user.first_name = clean['first_name']
                user.last_name = clean['last_name']
                user.email = clean['email']
                user.set_password(clean['password'])
                user.save()
                profile.course=clean['course']
                profile.contact_no=clean['contact_no']
                profile.birth_date=clean['birth_date']
                profile.mother_name=clean['mother_name']
                profile.mother_contact=clean['mother_contact']
                profile.father_name=clean['father_name']
                profile.father_contact=clean['father_contact']
                profile.guardian_name=clean['guardian_name']
                profile.guardian_contact=clean['guardian_contact']
                profile.bunk = bunk
                profile.save()
                messages.success(request, "Success: A student profile has been edited")
            except:
                messages.warning(request, "An error occured while saving.")
            return HttpResponseRedirect(reverse('list_students'))
        else:
            messages.warning(request, "An error occured while saving.")
            return render(request, 'student_form.html', {'form': form} )
    else:
        form = StudentForm(initial = {
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'password': user.password,
            'course': profile.course,
            'contact_no': profile.contact_no,
            'birth_date': profile.birth_date,
            'mother_name': profile.mother_name,
            'mother_contact': profile.mother_contact,
            'father_name': profile.father_name,
            'father_contact': profile.father_contact,
            'guardian_name': profile.guardian_name,
            'guardian_contact': profile.guardian_contact,
            'bunk': profile.bunk
        })
        form.fields['username'].widget.attrs['readonly'] = True
        form.fields['bunk'].choices=Bunk.objects.get_available2(profile.bunk.id)
    return render(request, 'student_form.html', {'form': form} )

@login_required
def delete_student(request, username):
    user = User.objects.get(username=username)
    profile = Student.objects.get(user=user)
    profile.delete()
    user.delete()
    messages.success(request, "Success: A student has been removed")
    return HttpResponseRedirect(reverse('list_students'))

@login_required
def student_logs(request, username):
    user = User.objects.get(username=username)
    student = Student.objects.get(user=user)
    logs = Log.objects.filter(student=student)
    return render(request, 'student_logs.html', {'logs': logs, 'user': user})

@login_required
def logs(request):
    logs = Log.objects.order_by('-datetime')
    return render(request, 'logs.html', {'logs':logs})

@login_required
def my_logs(request, username):
    user = User.objects.get(username=username)
    student = Student.objects.get(user=user)
    logs = Log.objects.filter(student=student).order_by('-datetime')
    return render(request, 'student_logs.html', {'logs': logs})

@login_required
def my_profile(request, username):
    user = User.objects.get(username=username)
    student = Student.objects.get(user=user)
    return render(request, 'my_profile.html', {'student': student})

@login_required
def my_in(request, username):
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
        messages.success(request, "Success: You Signed In")
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'my_in.html')

@login_required
def my_out(request, username):
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
        messages.success(request, "Success: You Signed Out")
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'my_out.html')
