from typing import Any, Sequence

from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest

from .models import Student, Teacher, User


class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "email", "role"]

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).filter(role=Student.Role.STUDENT)


admin.site.register(User)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher)
# Student.objects.create_teacher(username='s3', password='s3')
# from app.models import Student, Teacher
# python manage.py shell
