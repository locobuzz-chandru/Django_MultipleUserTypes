from django.urls import path, include
from app import views

urlpatterns = [
    path('', views.root),
    path('teacher', views.add_teacher),
    path('student', views.add_student)
]
