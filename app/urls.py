from django.urls import path, include
from app import views
from app.permissions import create_teacher_group

urlpatterns = [
    path('', views.root),
    path('teacher', views.add_teacher),
    path('student', views.add_student),
    path('perm', create_teacher_group)
]
