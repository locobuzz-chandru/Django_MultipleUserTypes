from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from .models import Student, Teacher, User


class StudentAdmin(admin.ModelAdmin):

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        qs = super().get_queryset(request)
        if request.user.is_superuser or request.user.role == User.Role.TEACHER:
            return qs
        return qs.filter(id=request.user.id)


class TeacherAdmin(admin.ModelAdmin):

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(id=request.user.id)


admin.site.register(User)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
