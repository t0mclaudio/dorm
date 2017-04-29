from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^accounts/login/$', auth_views.login, {'template_name': 'login.html'}, name="login"),
    url(r'^accounts/logout/$', auth_views.logout, {'next_page': '/'}, name="logout"),
    url(r'^$', views.index, name='index'),

    # Admin Administrator
    url(r'^administrators/$', view=views.list_admins, name="list_admins"),
    url(r'^administrator/add/$', view=views.add_admin, name="add_admin"),
    url(r'^administrator/(?P<username>[a-zA-Z-_0-9]+)/$', view=views.admin_profile, name="admin_profile"),
    url(r'^administrator/(?P<username>[a-zA-Z-_0-9]+)/edit/$', view=views.edit_admin_profile, name="edit_admin_profile"),
    url(r'^administrator/(?P<username>[a-zA-Z-_0-9]+)/delete/$', view=views.delete_admin, name="delete_admin"),

    # Admin Bunks
    url(r'^bunks/$', view=views.list_bunks, name="list_bunks"),
    url(r'^bunk/add/$', view=views.add_bunk, name="add_bunk"),
    url(r'^bunk/(?P<id>[a-zA-Z-_0-9]+)/$', view=views.bunk, name="bunk"),
    url(r'^bunk/(?P<id>[a-zA-Z-_0-9]+)/edit/$', view=views.edit_bunk, name="edit_bunk"),
    url(r'^bunk/(?P<id>[a-zA-Z-_0-9]+)/delete/$', view=views.delete_bunk, name="delete_bunk"),

    # Admin Manager
    url(r'^managers/$', view=views.list_managers, name="list_managers"),
    url(r'^manager/add/$', view=views.add_manager, name="add_manager"),
    url(r'^manager/(?P<username>[a-zA-Z-_0-9]+)/$', view=views.manager_profile, name="manager_profile"),
    url(r'^manager/(?P<username>[a-zA-Z-_0-9]+)/edit/$', view=views.edit_manager_profile, name="edit_manager_profile"),
    url(r'^manager/(?P<username>[a-zA-Z-_0-9]+)/delete/$', view=views.delete_manager, name="delete_manager"),

    # Manager Student
    url(r'^students/$', view=views.list_students, name="list_students"),
    url(r'^student/add/$', view=views.add_student, name="add_student"),
    url(r'^student/(?P<username>[a-zA-Z-_0-9]+)/$', view=views.student_profile, name="student_profile"),
    url(r'^student/(?P<username>[a-zA-Z-_0-9]+)/edit/$', view=views.edit_student_profile, name="edit_student_profile"),
    url(r'^student/(?P<username>[a-zA-Z-_0-9]+)/delete/$', view=views.delete_student, name="delete_student"),
    url(r'^student/(?P<username>[a-zA-Z-_0-9]+)/logs/$', view=views.student_logs, name="student_logs"),

    # Manager Logs
    url(r'^logs/$', view=views.logs, name="logs"),

    # Student URL's
    url(r'^(?P<username>[a-zA-Z-_0-9]+)/profile/', view=views.my_profile, name="my_profile"),
    url(r'^(?P<username>[a-zA-Z-_0-9]+)/logs/', view=views.my_logs, name="my_logs"),
    url(r'^(?P<username>[a-zA-Z-_0-9]+)/log-in/', view=views.my_in, name="my_in"),
    url(r'^(?P<username>[a-zA-Z-_0-9]+)/log-out/', view=views.my_out, name='my_out'),
]
