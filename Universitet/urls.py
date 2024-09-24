from django.urls import path
from . import views


urlpatterns = [
    path('', views.main),
    path('kafedralar/<int:pk>', views.kafedra, name='kafedra'),
    path('groups/<int:pk>', views.group, name='group'),
    path('students/<int:pk>', views.student, name='student'),
    path('students/details/<int:pk>', views.student_details, name='student_details'),
    path('subjects', views.subject, name='subject'),
    path('teachers<int:pk>', views.teacher, name='teacher')
]