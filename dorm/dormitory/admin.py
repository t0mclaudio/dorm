from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Student)
admin.site.register(Log)

@admin.register(Bunk)
class BunkAdmin(admin.ModelAdmin):
    list_display = ('id', 'code')
