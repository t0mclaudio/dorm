from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^accounts/login/$', auth_views.login, {'template_name': 'login.html'}, name="login"),
    url(r'^accounts/logout/$', auth_views.logout, {'next_page': '/'}, name="logout"),
    url(r'^$', views.index, name='index'),
    url(r'^add-student/$', view=views.add_student, name="add_student"),
    url(r'^add-manager/$', view=views.add_manager, name="add_manager"),
    url(r'^students/$', view=views.students, name="students"),
    # Student URL's
    url(r'^(?P<username>[a-zA-Z-_0-9]+)/profile/', view=views.profile, name="profile"),
    url(r'^(?P<username>[a-zA-Z-_0-9]+)/logs/', view=views.student_logs, name="student_logs"),
    url(r'^(?P<username>[a-zA-Z-_0-9]+)/log-in/', view=views.student_in, name="student_in"),
    url(r'^(?P<username>[a-zA-Z-_0-9]+)/log-out/', view=views.student_out, name='student_out'),
]
