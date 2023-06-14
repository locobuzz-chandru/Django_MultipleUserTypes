from django.urls import path
from app import views

urlpatterns = [
    path('', views.root),
    path('teacher', views.add_teacher),
    path('student', views.add_student),
    path('login', views.login),
    path('create_group', views.create_group),
]
