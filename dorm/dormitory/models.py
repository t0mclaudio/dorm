from django.db import models
from django.contrib.auth.models import User

class BunkManager(models.Manager):
    def get_available(self):
        used = Student.objects.values_list('bunk', flat=True)
        bunks = self.all()
        obj = []
        for bunk in bunks:
            if bunk.id not in used:
                obj.append((bunk.id, bunk.code))
        return obj

    def get_available2(self, using):
        used = Student.objects.values_list('bunk', flat=True)
        bunks = self.all()
        obj = []
        for bunk in bunks:
            if bunk.id not in used or bunk.id == using:
                obj.append((bunk.id, bunk.code))     
        return obj

# Create your models here.
class Bunk(models.Model):
    code = models.CharField(max_length=12, unique=True)

    objects = BunkManager()
    def __str__(self):
        return self.code

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    course = models.CharField(max_length=32)
    contact_no = models.CharField(max_length=16, verbose_name="Contact Number")
    birth_date = models.DateField(null=True, blank=True)
    mother_name = models.CharField(max_length=64)
    mother_contact = models.CharField(max_length=16, verbose_name="Contact Number")
    father_name = models.CharField(max_length=64)
    father_contact = models.CharField(max_length=16, verbose_name="Contact Number")
    guardian_name = models.CharField(max_length=64)
    guardian_contact = models.CharField(max_length=16, verbose_name="Contact Number")
    bunk = models.OneToOneField(Bunk)

    def __str__(self):
        name = "{} {}".format(self.user.first_name, self.user.last_name)
        return name

class Log(models.Model):
    student = models.ForeignKey(Student)
    log_type = models.CharField(max_length=4)
    datetime = models.DateTimeField(auto_now=False)
    destination = models.CharField(max_length=120, blank=True, null=True)
